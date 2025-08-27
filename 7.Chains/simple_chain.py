from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field   
from langchain_openai import ChatOpenAI
from langchain.output_parsers import StructuredOutputParser , ResponseSchema
from dotenv import load_dotenv


load_dotenv()

#model
model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)


# define schema 
schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the cricketer"),
    ResponseSchema(name="fact_2", description="fact 2 about the cricketer"),
    ResponseSchema(name="fact_3", description="fact 3 about the cricketer")
]

# define parser
parser = StructuredOutputParser.from_response_schemas(schema)


# prompt template
template = PromptTemplate(
    template="give any 3 facts about this cricketer {cricketer}\n{format_instructions}",
    input_variables=["cricketer"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain
chain = template | model | parser   
# invoke
result = chain.invoke({"cricketer": "Dhoni"})

#to visualize the chain

chain.get_graph().print_ascii()

print(result)