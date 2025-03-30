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
Find k smallest numbers 
'''
arr = [1,2,3,1,4, 3, 56]
def find_min(arr,k,remove_dupes):
    arr.sort()
    print("sorted",arr)
    if(remove_dupes==True):


        x = 1  
        
        for i in range(1, len(arr)):
            if arr[i] != arr[i - 1]:
                arr[x] = arr[i]
                x += 1
        
  
    min_k=[]
    for i in range(k):
        min_k.append(arr[i])
    
    return min_k
def find_min_native(arr):
    min=arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min=arr[i]
    return min
#print(find_min(arr,2,True))
#print(find_min_native(arr))
'''


'''
data = [[2, 20],[3, 30],  [1,10],[10, 110]]
def knn(data,x,k):
    diff=[]
    diff1=[]
    #print(data)
    for i in range(len(data)):
        #print(abs(data[i][0] -x))
        diff.append(abs(data[i][0] -x))
    min=[]
    print(diff)
    diff1=diff[:]
    print(diff1)
    min=find_min(diff,k,True)
    print(min)
    index=[]
  
    for m in range(len(min)):
        
        for j in range(len(diff1)):
            if diff1[j]==min[m]:
                index.append(j)
               # str=j+1
                break
    print(index)
    out=[]
    for k in index:
        out.append(data[k][1])


    return out



print(knn(data,1.5,2))