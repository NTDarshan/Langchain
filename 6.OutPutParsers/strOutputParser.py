from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)
#promt 1

template1 = PromptTemplate(
    template="write a detailed report on topic {topic}?",
    input_variables=["topic"]
)


#promt 2

template2 = PromptTemplate(
    template="write a 5 line summary on the following text \n {text}?",
    input_variables=["text"]
)


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model |  parser

result = chain.invoke({"topic": "black hole"})

print(result)
