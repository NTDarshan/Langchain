from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv


load_dotenv()

#model
model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

#parser 
parser = StrOutputParser()

#promts
prompt1 = PromptTemplate(
    template="give me a short summary of this topic {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="give me a 5 pointer summary of this text {text}",
    input_variables=["text"]
)

#chain
chain1 = prompt1 | model | parser | prompt2 | model | parser


#invoke the chain
result = chain1.invoke({"topic": "Sex Education"})
print(result)


