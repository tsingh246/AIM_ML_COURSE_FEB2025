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
