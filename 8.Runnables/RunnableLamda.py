from langchain_core import output_parsers
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel , RunnableSequence , RunnablePassthrough , RunnableLambda

load_dotenv()

pass_through = RunnablePassthrough()

def count_words(sentence: str) -> int:
    word_count = len(sentence.split())
    return word_count

prompt1= PromptTemplate(
    template="Tell me a joke about this :{joke}",
    input_variables=["joke"]    
)


model = ChatOpenAI()

output_parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt1, model, output_parser)

parallel_chain = RunnableParallel({
    "joke": RunnablePassthrough(),
    "count": RunnableLambda(count_words)
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chain.invoke({"joke": "AI"})
print( "joke is : " , result["joke"])
print( "count is : " , result["count"])
