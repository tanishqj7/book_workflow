import chromadb

client = chromadb.Client()
collection = client.get_or_create_collection("book_chapters")

def store_version(text, version_type, chapter_id):
    collection.add(
        documents=[text],
        ids=[f"{chapter_id}_{version_type}"],
        metadatas=[{"chapter": chapter_id, "version": version_type}]
    )

def get_versions(chapter_id):
    results = collection.get(where={"chapter": chapter_id})
    return results
