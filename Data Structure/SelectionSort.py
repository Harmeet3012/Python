list = [48,16,79,55,31,62]
print("Initial list ",list)

for i in range(len(list)-1):
    min = list[i]
    for j in range(i+1,len(list)):
        if min > list[j]:
            min = list[j]
            list[j]=list[i]
            list[i]=min

print("Final list using Selection Sort ",list)