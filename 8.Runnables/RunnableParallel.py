from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel , RunnableSequence

load_dotenv()

promt1 =  PromptTemplate(
    template="Generate a twitter post about this topic:{topic}",
      input_variables=["topic"]
)
llm1 = ChatOpenAI()
output_parser1 = StrOutputParser()


promt2 = PromptTemplate(
    template="Generate a linkdin post about this topic:{topic}",
    input_variables=["topic"]
)
llm2 = ChatOpenAI()
output_parser2 = StrOutputParser()

parallel_chain = RunnableParallel({ "tweet" :RunnableSequence(promt1, llm1, output_parser1), "linkdin":RunnableSequence(promt2, llm2, output_parser2)})

result = parallel_chain.invoke({"topic": "AI"})
# print(result)
print(result["tweet"])
