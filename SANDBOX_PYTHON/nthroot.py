'''
This program is to d=find nth root for a number
It takes 3 arguments the root to find, number and tolerance
Assumptions :
    root > 1, number >=0
'''
def nthrt(root,number,tolerance):
     if number >= 1:
        min= 1
        max=number
     elif number==0:
        min= 0
        max=0
     else:
        min= 0
        max=1
         
     #print(min,max,number)
       
     while(True):
        mid=(min+max)/2
        if mid**root == number:
            break
        elif abs(mid**root - number) < 0.0001:
           break
        elif mid**root > number:
            max=mid
        else:
            min =mid
     return round(mid ,4)   


print(nthrt(2,0,.0001))
