from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough

load_dotenv()

pass_through = RunnablePassthrough()

prompt1= PromptTemplate(
    template="Tell me a joke about this :{joke}",
    input_variables=["joke"]    
)

promp2= PromptTemplate(
    template="explain this joke in simple words :{joke}",
    input_variables=["joke"]
)
model = ChatOpenAI()

output_parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model, output_parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "explanation": RunnableSequence(promp2, model, output_parser)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"joke": "AI"})
print(result["joke"])
print(result["explanation"])
