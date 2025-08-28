from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from typing import Literal
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from dotenv import load_dotenv


load_dotenv()

#model 
model = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0
)

class review(BaseModel):
    sentiment : Literal['positive','negative'] = Field(description="The sentiment of the review")

#parser
parser = StrOutputParser()

#pydantic parser
pydantic_parser = PydanticOutputParser(pydantic_object=review)


#prompt1 template
prompt1 = PromptTemplate(
    template="classify the given customer into pasitive or negative review {review} \n {format_instructions}",
    input_variables=["review"],
    partial_variables={"format_instructions": pydantic_parser.get_format_instructions()}
)


prompt2 = PromptTemplate(
    template=(
        "Write a short, polite thank-you message in response to this positive review:\n\n"
        "{review}\n\n"
        "Keep it brief (1–2 sentences)."
    ),
    input_variables=["review"]
)


prompt3 = PromptTemplate(
    template=(
        "Write a short, polite apology message in response to this negative review:\n\n"
        "{review}\n\n"
        "Keep it brief (1–2 sentences) and show empathy."
    ),
    input_variables=["review"]
)
#chain
classifier_chain = prompt1 | model | pydantic_parser


branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: f"i don't know the sentiment of this review {x}")
)

final_chain = classifier_chain | branch_chain

review = "this is a fucking product"
result =  final_chain.invoke({"review": review})

print(result)
