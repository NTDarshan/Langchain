from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0.7
)

# parser
parser = JsonOutputParser()

# prompt template
template = PromptTemplate(
    template="give me age, role, nation of a cricketer {cricketer}\n{format_instructions}",
    input_variables=["cricketer"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# chain
chain = template | model | parser

# invoke
result = chain.invoke({"cricketer": "Dhoni"})

print(result)
