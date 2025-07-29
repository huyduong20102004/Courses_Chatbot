from qdrant_client import QdrantClient
import config  # import thông tin từ file config.py

# Kết nối Qdrant
client = QdrantClient(
    url=config.QDRANT_URL,
    api_key=config.QDRANT_API_KEY
)

# Kiểm tra ping
try:
    response = client.get_collections()
    print("Kết nối thành công! Danh sách collections:", response)
except Exception as e:
    print("Kết nối thất bại:", e)

