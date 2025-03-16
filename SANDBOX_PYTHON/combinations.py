'''
Given a list of people, find the number of handshakes
list ["A","B","C"]
Output: ["AB","AC","BC"]
# for k= 2
'''

list = ["A","B","C","D","E"]
out_list_2=[]
for i in range(len(list)):
    #print(list[i])
    for j in range(i+1,len(list)):
        out_list_2.append(list[i]+list[j])
        #print(list[i]+list[j])
print(out_list_2)
# for k= 3

out_list_3=[]
for i in range(len(list)):
    #print(list[i])
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            out_list_3.append(list[i]+list[j]+list[k])
        #print(list[i]+list[j])
print(out_list_3)

# for k= 4

out_list_4=[]
for i in range(len(list)):
    #print(list[i])
    for j in range(i+1,len(list)):
        for k in range(j+1,len(list)):
            for l in range(k+1,len(list)):
                out_list_4.append(list[i]+list[j]+list[k]+list[l])
        #print(list[i]+list[j])
print(out_list_4)
    

