from qdrant_client import QdrantClient
from config import QDRANT_URL, QDRANT_API_KEY

def clear_all_collections():
    # Kết nối Qdrant
    client = QdrantClient(url=QDRANT_URL, api_key=QDRANT_API_KEY)

    # Lấy danh sách tất cả collection
    collections = client.get_collections().collections
    if not collections:
        print(" There are no collections in Qdrant.")
        return

    print(" Deleting all collections from Qdrant:")
    for col in collections:
        print(f" - {col.name}")

    # Tiến hành xoá từng collection
    for col in collections:
        client.delete_collection(col.name)
        print(f" Deleted collection: {col.name}")

    print("\n All collections have been deleted from Qdrant.")

if __name__ == "__main__":
    clear_all_collections()

