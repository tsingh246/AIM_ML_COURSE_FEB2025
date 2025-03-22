'''

For equation:
    4x + 2y + z = 5
    x - 3y - z = 3
    3x + 2y + 2z = 10

eqns = [
    [4, 2, 1, 5],
    [1, -3, -1, 3]
    [3, 2, 2, 10]
]
```
result = solve_equations(eqns) 

result

'''


#scaler with list
def list_scaler_op(list,op,n):
    new_list=[]
    if op=="*":        
        for i in range(len(list)):
            #print(i)
            new_list.append(list[i]*n)
    return new_list

#print(list_op([4,10],"*",2))            

# Substrat a list from another element by element and remozeroes from resulting array output.
def list_op(l1,l2,op,remove_zero):
    out=[]
    if op=="-":
        
        for i in range(len(l1)):
            if remove_zero==True:
                if l1[i] - l2[i]!=0:
                    out.append(l1[i] - l2[i])
            else:
                out.append(l1[i] - l2[i])
        if l1[len(l1) -1] - l2[len(l1) -1] ==0:
            out.append(0)
    return out
#print(list_op([-16.0, 12.0, -96.0],[-9.0, 12.0, -96.0],"-",True))
ip3=[[4, 2, 1, 5],[1, -3, -1, 3],[3, 2, 2, 10]]
ip2=[[2,3,13],[3,2,12]]
#ip2=[[4,-3,24],[3,-4,32]]
ip1=[[4,10]]

def eliminate_variable(ip):
    global output
    after_elimination=[]
    output=[]
    if len(ip)==1:
        output.append([ip[0][len(ip) -2] / ip[0][len(ip) -1]])
        print("eliminate_variable ********* ",output)
        

    else:
        
        for j in range(1,len(ip)):
            #print(0,j)
            inner_len=len(ip[0])
            m= ip[0][inner_len -2] * ip[j][inner_len -2]
            m1=m / ip[0][inner_len -2]
            m2= m / ip[j][inner_len -2] 
            #print(m,m1,m2)
            #print(list_scaler_op(ip[0],"*",m1))
            #print(list_scaler_op(ip[j],"*",m2))
            new_input= list_op(list_scaler_op(ip[0],"*",m1),list_scaler_op(ip[j],"*",m2),"-",True)
            #print(new_input)
            after_elimination.append(new_input)
        print(after_elimination)
        eliminate_variable(after_elimination) 
    return output[0]
#eliminate_variable(ip3)

# ip3=[[4, 2, 1, 5],[1, -3, -1, 3],[3, 2, 2, 10]]
def solve_equations(ip):
    result=[]
    
    for i in range(len(ip)):
        modified_ip=ip[:len(ip) - i]
        print(modified_ip)
        if len(result) ==0:
            output= eliminate_variable(modified_ip)
            result.append(output)
        else:
            print("modufy arrays",modified_ip)
        
    return result

print(solve_equations(ip3))
