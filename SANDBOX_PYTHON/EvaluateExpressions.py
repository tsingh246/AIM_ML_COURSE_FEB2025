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

def find_index(arr,element):
    index=[]
    for i in range(len(arr)):
        if arr[i]==element:
            index.append(i)
    return index




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
input_str="15/5*2+10/2" # 16
op_seq=["/","*","+","-"]
op_arr,n_arr = read_expressions(input_str)
print(op_arr,n_arr)
for op in op_seq:
    index=find_index(op_arr,op)
    print(index)
    for i in range(len(index)):
        print(index[i])
        j=0
        if i == 0:
            j=index[i]
        else:
            j=index[i]-1
        print(j)
        var1=n_arr[j]
        var2=n_arr[j+1]
        val=exec_op(var1,var2,op_arr[j])
        print(val)
        #replacement=str(var1)+op_arr[i]+str(var2)
        #input_str=input_str.replace(replacement,str(val))
        #print(input_str) my_list[:index_to_remove] + my_list[index_to_remove+1:]
        op_arr= op_arr[:j] + op_arr[j+1:]
        n_arr=n_arr[:j] +n_arr[j+2:]
        n_arr.insert(j,val)
        
        print(op_arr,n_arr)





'''


    for op in op_seq:
        #print(op)
        for i in range(len(op_arr)):
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

'''