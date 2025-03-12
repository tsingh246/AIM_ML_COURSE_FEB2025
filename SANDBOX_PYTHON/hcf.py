'''
Find HCF of 2 numbers
HCF - Highest common factor
'''

def hcf(a,b):
    divisor = a
    dividend = b

    while True:
        remainder = dividend % divisor 
        print(remainder)
        if(remainder != 0):
            dividend = divisor
            divisor = remainder
        else:
            return divisor
        
print(hcf(30,75))

