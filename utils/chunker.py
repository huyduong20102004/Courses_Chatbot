import re
from docx import Document

# Field mapping from Vietnamese labels to keys
FIELD_MAPPING = {
    "Khóa học yêu cầu": "course-request",
    "Mục tiêu": "course-objective",
    "Công cụ AI sử dụng": "course-tools",
    "Thời lượng": "course-duration",
    "Người giảng dạy": "course-lecturer",
    "Nội dung": "course-content",
    "Lợi ích, ứng dụng thực tế": "course-benefits",
    "Học phí": "course-tuition"
}

def load_and_chunk_course_data(docx_path):
    document = Document(docx_path)
    lines = [p.text.strip() for p in document.paragraphs if p.text.strip()]

    all_chunks = []
    current_course_title = ""
    current_course_index = -1
    current_course_data = {}

    course_header_pattern = re.compile(r"^\d+\.\s+Khóa học:\s+(.*)$")

    for i in range(len(lines)):
        line = lines[i]
        match = course_header_pattern.match(line)
        if match:
            if current_course_data:
                all_chunks += extract_fields_from_course(
                    current_course_data, current_course_title, current_course_index
                )
                current_course_data = {}

            current_course_index += 1
            original_title = match.group(1).strip()
            current_course_title = (
                f"Khóa học: {original_title}"
                if not original_title.lower().startswith("khóa học")
                else original_title
            )

            # ❌ Không thêm field "Tên khóa học" ở đây nữa (theo yêu cầu)

            continue

        for field in FIELD_MAPPING:
            if line.startswith(field + ":") or line == field:
                value = line.split(":", 1)[-1].strip() if ":" in line else ""
                current_field = field
                current_course_data[current_field] = value

                j = i + 1
                while j < len(lines):
                    next_line = lines[j]
                    is_new_field = any(
                        next_line.startswith(f + ":") or next_line == f for f in FIELD_MAPPING
                    )
                    is_new_course = course_header_pattern.match(next_line)
                    if is_new_field or is_new_course:
                        break
                    current_course_data[current_field] += "\n" + next_line.strip()
                    j += 1
                break

    if current_course_data:
        all_chunks += extract_fields_from_course(
            current_course_data, current_course_title, current_course_index
        )

    return all_chunks

def format_noidung_field(text):
    lines = [line.strip() for line in text.splitlines() if line.strip() and line.strip() != "-"]
    joined = " ".join(lines)
    parts = re.split(r'(Module\s+\d+[:：]?|Phần\s+\d+[:：])', joined, flags=re.IGNORECASE)
    if len(parts) > 1:
        return "\n".join(f"- {parts[i].strip()} {parts[i+1].strip()}" for i in range(1, len(parts), 2)).strip()
    return "\n".join(f"- {line}" for line in lines).strip()

def extract_fields_from_course(course_data, course_title, index):
    chunks = []
    for field in FIELD_MAPPING:
        content = course_data.get(field, "").strip()
        if not content:
            continue
        if field == "Nội dung":
            content = format_noidung_field(content)
        chunks.append({
            "ten_khoa_hoc": course_title,
            "course_index": index,
            "field": field,
            "value": content,
            "metadata": {
                "ten_khoa_hoc": course_title.rstrip(".")
            }
        })
    return chunks







