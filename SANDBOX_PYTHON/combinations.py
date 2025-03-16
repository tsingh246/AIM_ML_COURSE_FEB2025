'''
Given a list of people, find the number of handshakes
list ["A","B","C"]
Output: ["AB","AC","BC"]
'''

list = ["A","B","C","D"]
out_list=[]
for i in range(len(list)):
    #print(list[i])
    for j in range(i+1,len(list)):
        out_list.append(list[i]+list[j])
        #print(list[i]+list[j])
print(out_list)
    

