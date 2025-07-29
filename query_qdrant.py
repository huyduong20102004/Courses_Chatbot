from qdrant_client import QdrantClient
from qdrant_client.http import models as rest
from sentence_transformers import SentenceTransformer
from collections import OrderedDict
import unicodedata
import re
import uuid

# ✅ Khởi tạo model chỉ 1 lần
MODEL = SentenceTransformer("VoVanPhuc/sup-SimCSE-VietNamese-phobert-base")

# ✅ Field mapping
field_aliases = {
    "thời lượng": "Thời lượng",
    "học phí": "Học phí",
    "người giảng dạy": "Người giảng dạy",
    "nội dung": "Nội dung",
    "mục tiêu": "Mục tiêu",
    "lợi ích": "Lợi ích, ứng dụng thực tế",
    "yêu cầu": "Khóa học yêu cầu",
    "công cụ": "Công cụ AI sử dụng",
    "tên khóa học": "Tên khóa học"
}

# ✅ Thứ tự chuẩn để hiển thị các field
field_order = [
    "Nội dung",
    "Thời lượng",
    "Mục tiêu",
    "Lợi ích, ứng dụng thực tế",
    "Công cụ AI sử dụng",
    "Khóa học yêu cầu",
    "Học phí",
    "Người giảng dạy",
]

# ✅ Format lại phần nội dung
def format_noidung_field(text):
    lines = [line.strip(" -") for line in text.splitlines() if line.strip() and line.strip() != "-"]
    joined = " ".join(lines)
    parts = re.split(r'(Module\s+\d+[:：]?|Phần\s+\d+[:：])', joined, flags=re.IGNORECASE)
    if len(parts) > 1:
        return "\n".join(f"- {parts[i].strip()} {parts[i+1].strip()}" for i in range(1, len(parts), 2)).strip()
    return "\n".join(f"- {line}" for line in lines).strip()

# ✅ Format lại các field khác
def format_field_value(field, value):
    value = value.strip()
    if field == "Nội dung":
        return format_noidung_field(value)
    lines = [line.strip(" -") for line in value.splitlines() if line.strip()]
    return "\n".join(f"- {line}" for line in lines)

# ✅ Chuẩn hóa text
def normalize(text):
    text = re.sub(r'[:：.,;!?…]', '', text)
    return re.sub(r'\s+', ' ', text.lower().strip())

# ✅ Tách field và tên khoá học từ câu hỏi
def extract_fields_and_titles(question, all_titles):
    lowered = question.lower()
    found_fields = list(OrderedDict.fromkeys(field_aliases[k] for k in field_aliases if k in lowered))
    normalized_title_map = {normalize(title): title for title in all_titles}

    if "khoá học" not in lowered and "khoa hoc" not in lowered:
        return found_fields, []

    raw_query = lowered.split("khoá học", 1)[-1] if "khoá học" in lowered else lowered.split("khoa hoc", 1)[-1]
    keywords = re.split(r',| và | hoặc | or ', raw_query)
    keywords = [normalize(kw.strip()) for kw in keywords if kw.strip()]

    if not keywords:
        return found_fields, all_titles

    matched = []
    for norm_title, original_title in normalized_title_map.items():
        match_count = sum(kw in norm_title for kw in keywords)
        if match_count:
            matched.append((match_count, original_title))
    matched.sort(reverse=True)
    found_titles = [title for _, title in matched]

    return found_fields, list(OrderedDict.fromkeys(found_titles))

# ✅ Chèn chunks vào Qdrant
def insert_chunks_into_qdrant(chunks, QDRANT_URL, QDRANT_API_KEY, collection_name="khoa-hoc"):
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=rest.VectorParams(size=768, distance=rest.Distance.COSINE)
    )

    points = []
    for chunk in chunks:
        vector = MODEL.encode(chunk["value"]).tolist()
        points.append(rest.PointStruct(
            id=str(uuid.uuid4()),
            vector=vector,
            payload={
                "ten_khoa_hoc": chunk["ten_khoa_hoc"],
                "field": chunk["field"],
                "value": chunk["value"]
            }
        ))
    client.upsert(collection_name=collection_name, points=points)

# ✅ Hàm truy vấn chính
def query_qdrant(question, QDRANT_URL, QDRANT_API_KEY, collection_name="khoa-hoc", top_k=200):
    query_vector = MODEL.encode(question).tolist()
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # Lấy tất cả tiêu đề khoá học
    all_points = client.scroll(collection_name=collection_name, with_payload=True, limit=1000)[0]
    all_titles = sorted(set(p.payload.get("ten_khoa_hoc") for p in all_points if "ten_khoa_hoc" in p.payload))
    target_fields, course_titles = extract_fields_and_titles(question, all_titles)

    # Semantic Search
    results = client.search(
        collection_name=collection_name,
        query_vector=query_vector,
        limit=top_k,
        with_payload=True
    )

    if not results:
        return "⚠️ Không tìm thấy kết quả phù hợp."

    course_map = OrderedDict()
    for point in results:
        payload = point.payload
        title = payload.get("ten_khoa_hoc")
        field = payload.get("field")
        value = payload.get("value", "")

        if not title or not field:
            continue
        if course_titles and title not in course_titles:
            continue
        if target_fields and field not in target_fields:
            continue

        if title not in course_map:
            course_map[title] = []
        course_map[title].append((field, value))

    if not course_map:
        return "⚠️ Không có dữ liệu phù hợp với tiêu chí truy vấn."

    # ✅ Hiển thị kết quả
    lines = []
    lines.append("📌 Kết quả Semantic Search:")
    lines.append(f"\n🧪 Field(s): {target_fields if target_fields else 'Tất cả các trường thông tin'}")
    lines.append(f"🧪 Khóa học: {course_titles if course_titles else 'Tất cả các khoá học'}")

    for idx, (title, fields) in enumerate(course_map.items(), 1):
        lines.append(f"\n{idx}. Khóa học: {title}")
        sorted_fields = sorted(
            [f for f in fields if f[0] != "Tên khóa học"],
            key=lambda x: field_order.index(x[0]) if x[0] in field_order else 999
        )
        for field, val in sorted_fields:
            formatted_val = format_field_value(field, val)
            lines.append(f"\n🔹 {field}:\n{formatted_val}")

    return "\n".join(lines)



















































