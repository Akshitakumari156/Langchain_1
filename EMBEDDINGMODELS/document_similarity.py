from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document=["Delhi is the capital of India","Lucknow is the capital of Uttar Pradesh","Virat Kohli is the captain of Indian cricket team","MS dhoni is a former captain of Indian cricket team famous for his finishing ability","Rohit Sharma is knowm for his elegant batting style and is the current captain of Indian cricket team"]

query="tell me about virat kohli"

doc_embeddings=embeddings.embed_documents(document)
query_embedding=embeddings.embed_query(query)
scores=cosine_similarity([query_embedding], doc_embeddings)[0]
index,sc=sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
print(document[index])
print("Similarity Score is:",sc)