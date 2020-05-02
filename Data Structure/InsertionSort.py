list = [12,6,15,4,3,10,9,3,11]
print("Before Sorting :",list)
list.insert(0,-1) # insert -1 at the first place

for i in range(2,len(list)):
    temp = list[i]
    ind = i-1
    # print("Before while :",list)
    while temp < list[ind]:
        list[ind+1] = list[ind]
        # print("In while :",list)
        ind-=1
    list[ind+1] = temp
    # print("After while :",list)

list.__delitem__(0)
print("Final List :",list)
