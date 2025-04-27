from sentence_transformers import SentenceTransformer
import numpy as np

def cos_similarity(a,b):
    dot_product= np.dot(a,b)
    magnitude_a = np.linalg.norm(a)
    magnitude_b = np.linalg.norm(b)
    cos_similarity=dot_product /(magnitude_a * magnitude_b)
    return cos_similarity

def euc_dist(a,b):
    return np.linalg.norm(a - b)

model_name = "all-MiniLM-L6-v2" # Or another model from Hugging Face
model = SentenceTransformer(model_name)
'''text1 = "India is a great country"
text2 = "Bharat ek mahan desh hai"
text3 = "Indian ocean."
'''
text_arr=["India is a great country",
          "Bharat ek mahan desh hai",
          "Indian ocean."
          ]

embeddings=[]
for t in text_arr:
    embeddings.append(model.encode(t))

#print(embeddings)
'''
embedding1 = model.encode(text1)
embedding2 = model.encode(text2)
embedding3 = model.encode(text3)
'''
def text_similarity(func,embeddings):
    text_similarity=[]
    for i in range(len(embeddings)):
        for j in range(i+1,len(embeddings)):
            text_similarity.append((func(embeddings[i],embeddings[j])).tolist())
    return text_similarity

'''distance1=euc_dist(embedding1 , embedding2)
distance2=euc_dist(embedding1 , embedding3)
distance3=euc_dist(embedding2 , embedding3)
'''
print(text_similarity(euc_dist,embeddings))

print("*****************************************")

print(text_similarity(cos_similarity,embeddings))





