from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="messages"),
    ("human", "{input}"),
])
chat_history = []
#load the chat history 
with open("4.Prompts_in_langchain/chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())
    
formatted_prompt = chat_prompt.invoke({
    "messages": chat_history,
    "input": "What is my refund ?"
})

print(formatted_prompt)

#invoke the model
response = model.invoke(formatted_prompt)

#print the response
print(response.content)
