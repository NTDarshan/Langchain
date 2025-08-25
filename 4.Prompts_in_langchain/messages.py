from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="what is the capital city of karnatak?"),
]


AiMessage = model.invoke(messages)
messages.append(AIMessage(content=AiMessage.content))
print(messages)
