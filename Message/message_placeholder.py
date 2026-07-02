from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template=ChatPromptTemplate(
   [('system','YOu are a helpful {domain} assistant.'),
    MessagesPlaceholder(variable_name='chat_history'),
   ('human',"{query}")]
)

chat_history=[]

with open('Message/chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

chat_template.invoke({"domain":"Programming","query":"Explain in simple terms what is Python",'chat_history':chat_history})

print(chat_template)