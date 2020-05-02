list = [71,15,48,15,22]

top = 1

lower = []
upper = []
lower.insert(0,0)
upper.insert(0,len(list)-1)

def quick(list,n,beg,end):

    left = beg
    right = end
    loc = beg

    while True:

        while list[loc] <= list[right] and loc != right:
            right-=1

        if loc == right:
            return loc

        if list[loc] > list[right]:
            list[loc],list[right] = list[right],list[loc]
            loc = right

        while list[left] <= list[loc] and left != loc:
            left+=1

        if loc == left:
            return loc

        if list[left] > list[loc]:
            list[loc],list[left] = list[left],list[loc]
            loc = left

while top != 0:
    beg = lower[0]
    lower.pop(0)

    end = upper[0]
    upper.pop(0)

    top = top - 1

    loc = quick(list,len(list),beg,end)

    if beg < loc-1:
        top+=1
        lower.insert(top-1,beg)
        upper.insert(top-1,loc-1)

    if loc+1 < end:
        top+=1
        lower.insert(top-1,loc+1)
        upper.insert(top-1,end)

print(list)
