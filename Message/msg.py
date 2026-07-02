from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",temperature=1.5
)

message=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="write a 5line poem on cricket")
]

result=model.invoke(message)
message.append(AIMessage(content=result.content))

print(message)