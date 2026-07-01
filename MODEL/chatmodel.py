from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",temperature=1.5
)

response = model.invoke("write a 5line poem on cricket")
print(response.content)