from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

#invoke
response = llm.invoke("What is the capital city of America ?")
print(response)
