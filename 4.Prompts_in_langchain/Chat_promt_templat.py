from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} assistant."),
    ("human", " explain it in simple {user_input}"),
])

prompt = chat_prompt.invoke({
    "domain": "Cricket",
    "user_input": "What is the LBW ?"
})
print(prompt)
response = model.invoke(prompt)
print(response.content)
