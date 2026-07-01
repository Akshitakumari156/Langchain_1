from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document=["Delhi is the capital of India","Lucknow is the capital of Uttar Pradesh"]

vectors=embeddings.embed_documents(document)

print(str(vectors))