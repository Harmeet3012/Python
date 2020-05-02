list = [15,14,16,13,17,21]

for i in range(len(list)-1): # This is to bring the largest value to the end. It should be iterated 1 time less than the list length
    print("Iteration ",i+1," :",list)
    j=0
    for j in range(len(list)-1-i): # This compares two consecutive values
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
        print("\tSub Iteration ",j+1,": ",list)

print("------------------------------------------------------\nFinal List using Bubble Sort is: ",list)