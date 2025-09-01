from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda , RunnableBranch

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on this topic :{topic}",
    input_variables=["topic"]
)


prompt2 = PromptTemplate(
    template="Summarize the following topic :{topic}",
    input_variables=["topic"]
)


model = ChatOpenAI(temperature=0)

parser = StrOutputParser()

# report_gen_chain = RunnableSequence(prompt1, model, parser)

#Langchain Expression Language(LCEL)
report_gen_chain = prompt1 | model | parser   #we can use this instead of RunnableSequence because it is more readable




branch_chain = RunnableBranch(
    (lambda x: len(x.split()) > 10, RunnableSequence(prompt2 , model , parser)),
    RunnablePassthrough(),
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke({"topic": "Indian Education System"})
print(result)
