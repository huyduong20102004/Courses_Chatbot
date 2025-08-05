from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from query_qdrant import query_qdrant
from config import QDRANT_URL, QDRANT_API_KEY
from llama_client import generate_answer
import re

app = Flask(__name__)
CORS(app)

def fix_html_if_broken(html_text):
    """
    Sửa HTML đơn giản nếu bị thiếu thẻ đóng.
    """
    # Đóng <ul> nếu mở mà không đóng
    if "<ul>" in html_text and "</ul>" not in html_text:
        html_text += "</ul>"
    # Đóng <li> cuối nếu còn mở
    if html_text.count("<li>") > html_text.count("</li>"):
        html_text += "</li>"
    return html_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        user_question = data.get("question", "").strip()

        if not user_question:
            return jsonify({"answer": "⚠️ Bạn chưa nhập câu hỏi nào."})

        # ✅ Semantic Search
        semantic_result = query_qdrant(
            question=user_question,
            QDRANT_URL=QDRANT_URL,
            QDRANT_API_KEY=QDRANT_API_KEY,
            collection_name="khoa-hoc"
        )

        # ✅ Prompt rõ ràng cho LLM trình bày HTML đúng cấu trúc
        full_prompt = f"""
Bạn là một trợ lý AI trả lời câu hỏi về khóa học.

Hãy trả lời một cách rõ ràng, dễ đọc và trình bày bằng **HTML** hợp lệ:
- Dùng <ul> và <li> để liệt kê nếu cần
- Dùng <strong> để in đậm
- Dùng <br> để ngắt dòng khi cần
- Tuyệt đối không dùng markdown như ** ** hoặc * *

Dữ liệu liên quan:
{semantic_result}

Câu hỏi người dùng:
{user_question}

Trả lời (chỉ trả về HTML hoàn chỉnh):
"""

        # ✅ Gọi LLM
        llm_response = generate_answer(full_prompt).strip()

        # ✅ Nếu kết quả quá ngắn thì cảnh báo
        if len(llm_response) < 100:
            llm_response += "<br><em>⚠️ Câu trả lời có thể bị cắt giữa chừng. Vui lòng thử lại.</em>"

        # ✅ Sửa HTML nếu bị thiếu thẻ
        fixed_html = fix_html_if_broken(llm_response)

        return jsonify({"answer": fixed_html})

    except Exception as e:
        return jsonify({"error": f"❌ Lỗi xảy ra: {str(e)}"}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)











