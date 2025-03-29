'''
dot product
a= [1,2]
b= [3,4]
-- 1*3 + 2*4
'''
def dot_product(a,b):
    product=0
    for i in range(len(a)):
        product=product+a[i]*b[i]
    return product

a= [1,2]
b= [3,4]
#print(dot_product(a,b))

'''
convert a vector to unit vector by dividng each value by its length
convert_to_uv([3, 4])
[0.6, 0.8]
'''
import math
a=[3,4]

def to_uv(a):
    magnitude=0
    b=[]
    for i in range(len(a)):
        magnitude=magnitude+a[i]**2
    magnitude= math.sqrt(magnitude)
    
    for j in range(len(a)):
        b.append(a[j]/magnitude)
    return b
print(to_uv(a))


