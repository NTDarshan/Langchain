from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]
while True:
    user_input = input("User: ")
    chat_history.append(HumanMessage(content=user_input))   
    if "exit" in user_input.lower():
        break
    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI:", response.content)
print("Chat History:", chat_history)
