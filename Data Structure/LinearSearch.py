pos = -1

list = [12,8,16,4,9,56,29,34,42]
val = int(input("Enter the value to search :"))

def search(list,n):
    for i in range(len(list)):
        if n == list[i]:
            globals()['pos']=i+1
            return True
    else:
        return False


if search(list,val):
    print("Found at ",pos)
else:
    print("Not Found")