arr1=[10,230,890,40]
def shift_arr(arr,k):
    for i in range(len(arr)-k):
         x=  arr[i] + arr[i+k]
         arr[i] = x-arr[i]
         arr[i+k] = x-arr[i]
         #print(arr)
    return arr

print(shift_arr(arr1,2))