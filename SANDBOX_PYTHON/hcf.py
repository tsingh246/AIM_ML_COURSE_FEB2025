'''
Find HCF of 2 numbers
HCF - Highest common factor
'''

def hcf(a,b):
    if a<=b:
        divisor = a
        dividend = b
    else:
        divisor = b
        dividend = a
    while True:
        remainder = dividend % divisor 
        #print(remainder)
        if(remainder != 0):
            dividend = divisor
            divisor = remainder
        else:
            return divisor

'''
Find HCF for a list

'''
def hcf_list(list):
    if len(list) ==2:
        return hcf(list[0],list[1])
    base_hcf = hcf(list[0],list[1])
    for i in range(2,len(list)):
        new_hcf=hcf(base_hcf,list[i])
        base_hcf=new_hcf
    return new_hcf

list=[126,162,180]
#list=[1071,462]
print(hcf_list(list))