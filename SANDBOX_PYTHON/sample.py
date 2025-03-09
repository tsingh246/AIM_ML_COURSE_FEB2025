#from math import sqrt
#print("Hello")
# A function to find if a point "a" lies between two points "x1, x2" in one dimension
def is_online(x1,x2,a):
    dist= abs(x2-x1)
    dist1= abs(a-x1)
    dist2=abs(a-x2)
    if dist==dist1 + dist2:
        return True
    else:
        return False
    

''' 
print(is_online(1, 2, 0))
print(is_online(-1, 2, 0))
print(is_online(-1, -2, 0))
print(is_online(2, -1, 0))
print(is_online(6,5,5.5)) 
'''

# A functio to find if two lines are overlapping or touching in one dimension

def are_overlapping(x1,x2,x3,x4):
    a=is_online(x1,x2,x3)
    b=is_online(x1,x2,x4)
    c=is_online(x3,x4,x1)
    d=is_online(x3,x4,x2)

    if (a==True or b==True) or (c==True or d==True):
        return True
    else :
        return False
    
'''
print(are_overlapping(2,5,3,4))  
'''  




def sqrt(n):
    # a**2 < n < b**2
    if n >= 1:
        min= 1
        max=n
    else:
        min= 0
        max=1
     
    print(min,max,n)
     
        
    while(True):
        mid=(min+max)/2
       # print(mid)
        if mid**2 == n:
            break
        elif abs(mid**2 - n) < 0.0001:
           break
        elif mid**2 > n:
            max=mid
        else:
            min =mid
    return round(mid ,4)   


def cubrt(n):
    # a**2 < n < b**2
    if n >= 1:
        min= 1
        max=n
    else:
        min= 0
        max=1
       
    while(True):
        mid=(min+max)/2
        if mid**3 == n:
            break
        elif abs(mid**3 - n) < 0.0001:
           break
        elif mid**3 > n:
            max=mid
        else:
            min =mid
    return round(mid ,4)   


                

#print(sqrt(100))
#print(cubrt(1000))
def swap(x,y):
    y= x^y
    x=y^x
    y=y^x
    print(x,y)


#print(swap(10,20))


#print(x,y)
# circular shift array to left
arr1=[10,230,890,40]
def shift_arr(arr,k):
    for i in range(len(arr)-k):
         x=  arr[i] + arr[i+k]
         arr[i] = x-arr[i]
         arr[i+k] = x-arr[i]
         #print(arr)
    return arr



'''print(arr1)
print("############")
print(shit_arr(arr1,1))
print("------------------")
'''
#print(arr1)
print("############")
#arr2=shift_arr(arr1,3)

#print(arr2)

def reverse_array(arr):
    k=len(arr)
    for i in range(k):
        if (i<k-1-i):
                               
                arr[k-1-i]=arr[i] ^ arr[k-1-i]
                arr[i]=arr[k-1-i] ^ arr[i]
                arr[k-1-i]=arr[k-1-i] ^ arr[i]
        else:
            break
    
    print(arr)

reverse_array(arr1)