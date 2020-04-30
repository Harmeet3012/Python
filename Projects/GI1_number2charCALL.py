from Projects.GI1_number2char import *

n=int(input("Enter any number"))

if n<0:
    print("Positive number please")
    exit(0)
elif n<100:
    two(n)
elif n>=100 and n<1000:
    three(n)
elif n>=1000 and n<10000:
    four(n)
elif n>=10000 and n<1000000:
    fivesix(n)
elif n>=1000000 and n<1000000000:
    million(n)
elif n==1000000000:
    print("one Billion")
else:
    print("Out of Range")


