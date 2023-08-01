import chromadb

chroma_client = chromadb.Client()

collections = chroma_client.create_collection(name = "my_collection")

collections.add(
    documents = ["my name is akshath","my name is not akshath"],
    metadatas = [{"source":"my_source"},{"source":"my_source"}],
    ids = ["id1","id2"]
)

results = collections.query(
    query_texts = ["what is my name"],
    n_results = 1
)

print(results)