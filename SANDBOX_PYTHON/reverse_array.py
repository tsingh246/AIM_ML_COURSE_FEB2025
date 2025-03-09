def reverse_array(arr):
    k=len(arr)
    for i in range(k):
        if (i<k-1-i):
                print(i)               
                arr[k-1-i]=arr[i] ^ arr[k-1-i]
                arr[i]=arr[k-1-i] ^ arr[i]
                arr[k-1-i]=arr[k-1-i] ^ arr[i]
        else:
            break
    
    print(arr)
arr1=[10,230,890,40,90,30,20]
reverse_array(arr1)