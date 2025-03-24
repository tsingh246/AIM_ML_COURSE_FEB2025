'''
def matrix_mu(A, B):
    returns mat

A = [
        [1, 2],
        [2, 3]
    ]
B = [
        [3, 4, 7],
        [5, 6, 8],
    ]
> matrix_mu(A, B)

[[13, 16, 23],
[21, 26, 38]]```

'''

a=[[1, 2],[2, 3]]
b= [[3, 4, 7],[5, 6, 8]]

# a is 2*2 and b is 2*3
result=[]
for i in range(len(a)):
    result1=[]
    for j in range(len(b[i])):        
        s=0
        for k in range(len(b)):
            s=s+ a[i][k]*b[k][j]
            #print(a[i][k],b[k][j],s)
        result1.append(s)
    #print(result1)
    result.append(result1)

print(result)        #print(b[i][j])