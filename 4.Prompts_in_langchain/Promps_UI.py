from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate , load_prompt

load_dotenv()
model = ChatOpenAI(model="gpt-4", temperature=1.0 , max_completion_tokens=2000)

st.title("Research Tool!")


paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] ) 




template = load_prompt('4.Prompts_in_langchain/prompt_template.json')

if st.button("Submit"):
    chain = template | model
    response = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input,
    })
    st.write(response.content)
