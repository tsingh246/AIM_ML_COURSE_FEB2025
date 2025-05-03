'''
 Find the smallest value of a convex arra which first decreases and then increases:
 arr = [10, 9, 8, 6.5, 4.1, 3.2, 2, 4, 4.5, 6] 

 Ans: 2
'''

arr = [10, 9, 8, 6.5, 4.1, 3.2, 2, 4, 4.5, 6] 
#//4.1, 3.2, 2, 4, 4.5,6
l=len(arr) -1 
#print(l)

#print(mid)
min=0
max=l
while min != max:
    mid=int((min+max)/2)
    print(mid)
    if arr[mid] < arr[mid -1] and arr[mid] < arr[mid+1]:
        min=max=mid
    elif arr[mid] < arr[mid -1] and arr[mid] > arr[mid +1]:
        if mid+1 != l:
            min= mid
            max=l
        else:
            min=max=mid=mid+1
    elif arr[mid] > arr[mid -1] and arr[mid] < arr[mid +1]:
        min=0
        max= mid
 
print("------------------")
print(mid)
print(arr[mid])

    