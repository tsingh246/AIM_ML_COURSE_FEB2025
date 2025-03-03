print("Hello")
def get_factorial(n):
    if n<=1:
        return 1
    else:
        return n*get_factorial(n-1)
    

#print(get_factorial(5))

n=5
series=[]
for i in range(n):
    if i==0:
        series.append(0)
    elif i==1:
        series.append(1)
    else:
        series.append(series[i-2]+series[i-1])
print(series)