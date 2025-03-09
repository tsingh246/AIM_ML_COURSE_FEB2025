a= 2
b=4
print(a ^ b)

'''
Given three lists of numbers, 
return the list of their XORs
all three lists have same size

Input: xors([1, 2], [2, 3], [3, 4]):
Output: [0, 5]

'''

def xors(a,b,c):
    l=[]
    for i in range(len(a)):
        l.append(a[i] ^ b[i] ^ c[i])
    return l

print(xors([1, 2], [2, 3], [3, 4]))