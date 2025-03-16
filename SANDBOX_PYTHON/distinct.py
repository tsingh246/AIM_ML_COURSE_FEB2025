list=[2,3,5,3,2,5,2,3,8]

for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            list[j]=None

print(list)