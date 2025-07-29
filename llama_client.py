import os
import requests
from dotenv import load_dotenv

# ✅ Load API key từ file .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_answer(prompt, system_message="Bạn là một trợ lý AI lịch sự, viết tự nhiên như đang trò chuyện."):
    try:
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.3-70b-versatile",  # ✅ Model mạnh & miễn phí từ Groq
            "messages": [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 1000
        }

        # ✅ URL của Groq
        url = "https://api.groq.com/openai/v1/chat/completions"

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"❌ Lỗi khi gọi Groq API: {str(e)}"














