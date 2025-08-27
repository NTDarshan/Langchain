from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

#build an pydantics model
class cricketer(BaseModel):
    name: str = Field(description="name of the cricketer")
    age: int = Field(description="age of the cricketer")
    role: str = Field(description="role of the cricketer")
    nation: str = Field(description="nation of the cricketer")
    fact_1: str = Field(description="fact 1 about the cricketer")
    fact_2: str = Field(description="fact 2 about the cricketer")
    fact_3: str = Field(description="fact 3 about the cricketer")
    

# define parser
parser = PydanticOutputParser(pydantic_object=cricketer)

# prompt template
template = PromptTemplate(
    template="give me name, age, role, nation, 3 facts about a cricketer {cricketer}\n{format_instructions}",
    input_variables=["cricketer"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain
chain = template | model | parser

# invoke
result = chain.invoke({"cricketer": "Dhoni"})

print(result)
    