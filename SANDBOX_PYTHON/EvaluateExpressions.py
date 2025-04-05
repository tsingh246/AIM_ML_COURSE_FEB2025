def textToInt(str):
    num=0
    l=len(str)
    for i in range(l):
        num+=(ord(str[i]) - ord("0"))*(10**(l-1 - i))
    return num

def exec_op(var1,var2,op):
    if op == "/":
        return var1 / var2
    elif op ==  "*":
        return var1 * var2
    elif op == "+":
        return var1 + var2
    elif op == "-":
        return var1 - var2
    else:
        print("Incorrect operator")
    
input_str="15/5*2+10-4+10" # 16

def read_expressions(str):
    op=["/","*","+","-"]
    op_arr=[]
    n_arr=[]
    t_str=""

    for i in range(len(str)):
        #print(str[i])
        if input_str[i] in op:
            op_arr.append(str[i])
            n_arr.append(textToInt(t_str))
            t_str=""
        else:
            t_str=t_str+input_str[i]
            #n_arr.append(str[i])
    n_arr.append(textToInt(t_str))
    return op_arr,n_arr

#print(read_expressions(str))
#op_arr=['/', '*', '+']
#n_arr=[15, 5, 2, 10]
op=["/","*","+","-"]
op_arr,n_arr = read_expressions(input_str)

for op in op_arr:
    #print(op)
    for i in range(len(op)):
        if op==op_arr[i]:
            #print("found",op_arr[i],i)
            var1=n_arr[i]
            var2=n_arr[i+1]
            val=exec_op(var1,var2,op_arr[i])
            replacement=str(var1)+op_arr[i]+str(var2)
            input_str=input_str.replace(replacement,str(val))
            print(input_str)
            op_arr= op_arr[1:]
            n_arr=n_arr[2:]
            n_arr.insert(0,val)
            print(op_arr,n_arr)
            break


