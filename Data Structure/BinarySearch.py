pos = -1
list = [4,15,23,61,87,50,41,36,48,12,19,65]
list.sort()
print(list)
val = int(input("Enter the value to search :"))

def search(list,n):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        if n == list[mid]:
            globals()['pos']=mid+1
            return True
        elif n < list[mid]:
            high = mid-1
        else:
            low = mid+1

    return False

if search(list,val):
    print("Found at ",pos)
else:
    print("Not Found")