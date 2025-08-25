from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-large" , dimensions=32)

docs = ["india is a country in south asia", 
        "india won the cricket world cup 2023",
        "india is a country in south asia"]
doc_embeddings = embeddings.embed_documents(docs)
print(str(doc_embeddings))
print(len(doc_embeddings))

