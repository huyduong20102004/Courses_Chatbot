"""1
import os
import requests
from dotenv import load_dotenv

# ✅ Load API key từ .env
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_answer(prompt, system_message="Bạn là một trợ lý AI lịch sự, viết tự nhiên như đang trò chuyện."):
    try:
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "meta-llama/llama-3.3-70b-instruct",
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        response.raise_for_status()  # Gây lỗi nếu không phải 2xx

        return response.json()['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ Lỗi khi gọi mô hình: {str(e)}"
    



 
#app.py
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from query_qdrant import query_qdrant
from config import QDRANT_URL, QDRANT_API_KEY
from llama_client import generate_answer  # ✅ sửa ở đây
import re

app = Flask(__name__)
CORS(app)

def remove_markdown(text):
    """
    Loại bỏ **markdown** (bold, italic, header...) từ nội dung trả về của LLaMA
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
            return jsonify({"answer": "Bạn chưa nhập câu hỏi nào."})

        # ✅ Semantic Search
        semantic_result = query_qdrant(
            question=user_question,
            QDRANT_URL=QDRANT_URL,
            QDRANT_API_KEY=QDRANT_API_KEY,
            collection_name="khoa-hoc"
        )

        # ✅ Tạo prompt gửi sang LLaMA
        full_prompt = f"""Dựa trên thông tin sau, hãy trả lời câu hỏi một cách tự nhiên như đang trò chuyện:

Thông tin tìm được:
{semantic_result}

Câu hỏi:
{user_question}
"""

        # ✅ Gọi LLaMA
        llm_response = generate_answer(full_prompt)

        # ✅ Loại bỏ markdown trước khi trả về
        clean_response = remove_markdown(llm_response)

        return jsonify({"answer": clean_response})

    except Exception as e:
        return jsonify({"error": f"Lỗi xảy ra: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)

"""