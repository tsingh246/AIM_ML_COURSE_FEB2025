'''
This program is to find the power for a number
It takes 2 arguments the number and power
Assumptions :
    root > 1, number >=0
'''
def pow(number,power):

    if power == 0:
        return 1
    elif power < 0:
        return 1 / pow(number, -power)
    else:
        out = 1
        for i in range(power):
              
            out *= number
           
        return out

'''
This program is to d=find nth root for a number
It takes 3 arguments the root to find, number and tolerance
Assumptions :
    root > 1, number >=0
'''
def nthrt(root,number,tolerance):
     if root <= 1:
         print("Root must be greater than 1") 
     if number < 0 and root % 2 == 0:
         print("Cannot find even root of negative number")         
     if number == 1:
         return 1
     if number < 0 and root % 2 != 0:
         return -nthrt(root, -number, tolerance)
     if number >= 1:
        min= 1
        max=number
     elif number==0:
        min= 0
        max=0
     else:
        min= 0
        max=1
         
     print(min,max,number)
     iterations = 0
     while(True):
        iterations +=1
        mid=(min+max)/ 2
        if pow(mid,root) == number:
            break
        elif abs(pow(mid,root) - number) < tolerance:
           break
        elif pow(mid,root) > number:
            max=mid
        else:
            min =mid
     print("Number of iterations:", iterations)
     return round(mid ,4)   


print(nthrt(3,8,.0001))
#print(pow(2,5))
