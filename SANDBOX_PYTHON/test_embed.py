import ollama
import numpy as np
from sentence_transformers import SentenceTransformer

model_name = "all-MiniLM-L6-v2" # Or another model from Hugging Face
model = SentenceTransformer(model_name)


def cos_similarity(a,b):
    dot_product= np.dot(a,b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    cos_similarity=dot_product /(magnitude_a * magnitude_b)
    return cos_similarity

def euc_dist(a,b):
    return np.linalg.norm(a - b)

def get_embedding(text, model="nomic-embed-text"):
    response = ollama.embeddings(
        model=model,
        prompt=text
    )
    embedding = response['embedding']
    return np.array(embedding)


s1="King"
s2="Man"
s3="Woman"
s4="Queen"
e_s1=get_embedding(s1)
e_s2=get_embedding(s2)
e_s3=get_embedding(s3)
e_s4=get_embedding(s4)
#print(e_s1)

e1_s1=model.encode(s1)
e2_s2=model.encode(s2)
e3_s3=model.encode(s3)
e4_s4=model.encode(s4)
# check s1 - s2 +s3= s4

e_x= (e_s1 - e_s2) + e_s3
e_y= (e1_s1 - e2_s2) + e3_s3

b= np.array_equal(e_x, e_s4)
dist=euc_dist(e_x, e_s4)
print("------------------------------OLlama--------------------------")
print(b)
print(dist)
print("------------------------------ST----------------------------------")
by= np.array_equal(e_y, e4_s4)
disty=euc_dist(e_y, e4_s4)
print(by)
print(disty)


