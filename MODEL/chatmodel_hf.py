from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

# Invoke the endpoint directly
model = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    max_new_tokens=100,
    temperature=0.5
)

# Call it directly without ChatHuggingFace wrapping
result = model.invoke("What is the Capital of INDIA?")
print(result)