from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel


load_dotenv()


#defining models
model1 = ChatOpenAI(
    model_name="gpt-4o-mini",
    temperature=0.7
)

model2 = ChatOpenAI(
    model_name="gpt-4o",
    temperature=0.7
)   

#defining parsers
parser = StrOutputParser()

#defining prompts
prompt1 = PromptTemplate(
    template='generate short and simple notes for the following text \n {topic}?',
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='generate a 5 question answers for the following topic \n {topic}',
    input_variables=["topic"]
)

promp3 = PromptTemplate(
    template='merge the following notes and quiz and make a single document \n notes --> {notes} \n  quiz --> {quiz}',
    input_variables=["notes", "quiz"]
)

# parallel_chain = RunnableParallel(
#     notes=prompt1 | model1 | parser,
#     quiz=prompt2 | model2 | parser
# )

parallel_chain = RunnableParallel(
    {
        "notes": prompt1 | model1 | parser,
        "quiz": prompt2 | model2 | parser
    }
)

final_chain = parallel_chain | promp3 | model2 | parser

topic = """
Black holes are mysterious regions in space where gravity is so strong that nothing—not even light—can escape their pull. They are formed when massive stars exhaust their fuel and collapse under their own gravity, compressing matter into an infinitely dense point called a singularity, surrounded by a boundary known as the event horizon. Anything that crosses this horizon is lost forever to the black hole. Despite their invisible nature, black holes can be detected by observing their effects on nearby stars, gas, and light. They play a crucial role in shaping galaxies, influencing the motion of stars, and even producing powerful jets of energy. Modern research into black holes not only helps us understand the universe’s structure but also challenges our understanding of physics, space, and time itself.

Would you like me to make this **simpler for school-level explanation** or **more detailed for advanced understanding**?


"""
result = final_chain.invoke({"topic": topic})

print(result)

#save the result in a file
with open("black_hole.txt", "w") as f:
    f.write(result)


#visualize the chain
final_chain.get_graph().print_ascii()



