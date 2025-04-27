import ollama
import numpy as np

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


text_arr=["India is a great country",
          "Bharat ek mahan desh hai",
          "Indian ocean."
          ]

embeddings=[]
for t in text_arr:
    embeddings.append(get_embedding(t))

def text_similarity(func,embeddings):
    text_similarity=[]
    for i in range(len(embeddings)):
        for j in range(i+1,len(embeddings)):
            text_similarity.append((func(embeddings[i],embeddings[j])).tolist())
    return text_similarity

print(text_similarity(euc_dist,embeddings))

print("*****************************************")

print(text_similarity(cos_similarity,embeddings))