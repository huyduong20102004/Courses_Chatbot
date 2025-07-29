from utils.chunker import load_and_chunk_course_data
from query_qdrant import insert_chunks_into_qdrant
from config import QDRANT_URL, QDRANT_API_KEY
import os

def main():
    docx_path = "data/course_intro.docx"

    if not os.path.exists(docx_path):
        print(f"File not found: {docx_path}")
        return

    # Load and chunk course data from DOCX
    chunks = load_and_chunk_course_data(docx_path)

    if not chunks:
        print("No valid data found in the DOCX file.")
        return

    # Insert into Qdrant collection
    insert_chunks_into_qdrant(
        chunks=chunks,
        QDRANT_URL=QDRANT_URL,
        QDRANT_API_KEY=QDRANT_API_KEY,
        collection_name="khoa-hoc"  # You can rename this if needed
    )

    print(f"Inserted {len(chunks)} chunks into Qdrant.")

if __name__ == "__main__":
    main()















