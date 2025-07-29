from sentence_transformers import SentenceTransformer
import torch

class EmbeddingModel:
    def __init__(self, model_name='all-MiniLM-L6-v2', device=None):
        """
        Khởi tạo SentenceTransformer embedding model.
        Nếu device=None, tự động chọn GPU (nếu có), ngược lại dùng CPU.
        """
        if device is None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.model = SentenceTransformer(model_name, device=device)

    def encode(self, texts, batch_size=32):
        """
        Encode danh sách văn bản thành vector embedding.
        Trả về list các vector float.
        """
        vectors = self.model.encode(
            texts,
            show_progress_bar=False,
            batch_size=batch_size,
            convert_to_numpy=True,     # ✅ Đảm bảo trả về np.ndarray
            normalize_embeddings=True  # ✅ Cosine similarity chuẩn hơn
        )
        return vectors.tolist()        # ✅ Trả ra list (dễ serialize nếu dùng JSON)

    def encode_single(self, text: str):
        """
        Encode một văn bản đơn lẻ.
        """
        return self.encode([text])[0]


