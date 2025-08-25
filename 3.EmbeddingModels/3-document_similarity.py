from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()
embeddings = OpenAIEmbeddings(model="text-embedding-3-large" , dimensions=300)

documents = [
    "Sachin Tendulkar, known as the 'God of Cricket', played for India from 1989 to 2013. He is the highest run-scorer in international cricket and the only player to score 100 international centuries.",
    
    "Virat Kohli, one of the modern greats, has been praised for his consistency and aggressive batting style. He has numerous records across formats and led India to significant Test victories abroad.",
    
    "Mahendra Singh Dhoni, India's most successful captain, is known for his calm demeanor and sharp cricketing mind. He led India to win the 2007 T20 World Cup, 2011 ODI World Cup, and 2013 Champions Trophy.",
    
    "Kapil Dev, an all-rounder and former captain, led India to their first-ever Cricket World Cup victory in 1983. He was known for his powerful batting and fast-medium bowling.",
    
    "Rohit Sharma, famous for his elegant stroke play, holds the record for the highest individual score in ODIs — 264 runs. He has multiple double centuries in ODIs and is the current Indian captain."
]

query = 'tell me about virat kohli'

doc_embedding = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)


scores = cosine_similarity([query_embedding], doc_embedding)

index, score =  sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print(documents[index])
print("similarity score is :", score)








