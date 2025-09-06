



def f(x):
    return 4*x**2 + 5*x - 4

# equation is 4x^2 + 5x -4
def df(x):
    return 8*x + 5  


#print(f(-1))

lr= 0.001
epochs= 630
def findMin(f,lr,epochs):
    x= 0
    for i in range(epochs):
        print(i,x,f(x))
        left=f(x-lr)
        right=f(x+lr)
        if left < right:
            x = x - lr
        else:
            x = x + lr
    
    return x
print(findMin(f,lr,epochs))
print("Testing")
print(f(-0.625))
print(f(-0.624))
print(f(-0.626))
