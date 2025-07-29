from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from query_qdrant import query_qdrant
from config import QDRANT_URL, QDRANT_API_KEY
from llama_client import generate_answer  # ✅ Sử dụng Groq
import re

app = Flask(__name__)
CORS(app)

def remove_markdown(text):
    """
    Loại bỏ markdown như **bold**, *italic* khỏi phản hồi.
    """
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)  # Bỏ **text**
    text = re.sub(r'\*(.*?)\*', r'\1', text)      # Bỏ *text*
    return text

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

        # ✅ Tạo prompt gửi sang LLM
        full_prompt = f"""Dựa trên thông tin sau, hãy trả lời câu hỏi một cách tự nhiên như đang trò chuyện:

Thông tin tìm được:
{semantic_result}

Câu hỏi:
{user_question}
"""

        # ✅ Gọi LLM (Groq / Mixtral)
        llm_response = generate_answer(full_prompt)

        # ✅ Loại bỏ markdown
        clean_response = remove_markdown(llm_response)

        return jsonify({"answer": clean_response})

    except Exception as e:
        return jsonify({"error": f"❌ Lỗi xảy ra: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)











