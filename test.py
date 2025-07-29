# ✅ Fix Unicode khi in tiếng Việt (Windows)
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8')

from query_qdrant import query_qdrant
from config import QDRANT_URL, QDRANT_API_KEY

def main():
    # ✅ Câu hỏi mẫu
    query = "Cho tôi biết có tất cả bao nhiêu khoá học hiện có?"

    # ✅ Truy vấn
    result = query_qdrant(
        question=query,
        QDRANT_URL=QDRANT_URL,
        QDRANT_API_KEY=QDRANT_API_KEY,
        collection_name="khoa-hoc"
    )

    print("\n=== KẾT QUẢ ===")
    print(result)

if __name__ == "__main__":
    main()







