from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence


load_dotenv()

promt = PromptTemplate(
    input_variables=["topic"],
    template="tell me a joke about{topic}?"
)

model = ChatOpenAI()
output_parser = StrOutputParser()

promt1 =  PromptTemplate(
    template="explain this joke:{joke}",
      input_variables=["joke"]
)

chain = RunnableSequence(promt,model,output_parser , promt1 , model , output_parser)

result = chain.invoke({"topic": "India"})
print(result)
