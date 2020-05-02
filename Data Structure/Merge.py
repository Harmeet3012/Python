list1 = [1,4,9,12,16,25,35,37,42,46,49,50]
list2 = [2,13,14,18,23,29,30,32,39]
list3 = []

li1,li2=0,0

while li1 < len(list1) and li2 < len(list2):
    if list1[li1] <= list2[li2]:
        list3.append(list1[li1])
        li1 += 1

    else:
        list3.append(list2[li2])
        li2 += 1

    if li1 >= len(list1):
        for li2 in range(li2,len(list2)):
            list3.append(list2[li2])

    if li2 >= len(list2):
        for li1 in range(li1,len(list1)):
            list3.append(list1[li1])

print(list1)
print(list2)
print("The merged list is : \n",list3)