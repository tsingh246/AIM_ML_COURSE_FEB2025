'''
ou are given two lists of numbers: Actual and Predicted First Code up Mean absolute error and mean squared error.

def mean_squared_error(actual, predicted):
    # your code

def mean_absolute_error(actual, predicted):
    # Your code

'''
a = [4,2,3]
b = [3, 2, 4]
def mean_abs_error(a,b):
    abs_error=0
    for i in range(len(a)):
        abs_error=abs_error+abs(a[i] -b[i])
    return abs_error/len(a)
  
#print(mean_abs_error(a,b))

def mean_sq_error(a,b):
    abs_error=0
    for i in range(len(a)):
        abs_error=abs_error+(a[i] -b[i])**2
    return abs_error/len(a)

#print(mean_sq_error(a,b))

'''

'''
arr = [1,2,3,4, 3, -2, 56]
def find_min(arr,k):
    arr.sort()
    min_k=[]
    for i in range(k):
        min_k.append(arr[i])
    return min_k

print(find_min(arr,2))

