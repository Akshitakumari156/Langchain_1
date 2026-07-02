from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import HumanMessage, SystemMessage

chat_Template=ChatPromptTemplate([
    ('system', "You are a helpful {domain} assistant."),
    ('human', "Explain in simple terms what is {topic}")
    # SystemMessage(content="You are a helpful  {domain} assistant."),
    # HumanMessage(content="Explain in simple terms what is {topic}")
])

prompt=chat_Template.invoke({"domain": "programming", "topic": "Python"})

print(prompt)