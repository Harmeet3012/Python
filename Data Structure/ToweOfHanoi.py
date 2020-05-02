A = [4,3,2,1] # Beginning
B = [] # Auxiliary
C = [] # Ending

print("A : ",A)
print("B : ",B)
print("C : ",C)

print("---------------------------------------------------\nStart Process\n")

N = len(A)

def TowerOfHanoi(N,beg,aux,end):

    if N==1:
        print("A : ", A)
        print("B : ", B)
        print("C : ", C)
        print("-------------------------------------------------")
        p = beg.pop()
        end.append(p)

    else:
        TowerOfHanoi(N-1,beg,end,aux)
        TowerOfHanoi(1,beg,aux,end)
        TowerOfHanoi(N-1,aux,beg,end)

TowerOfHanoi(N,A,B,C)

print("Process Ends\nA : ",A)
print("B : ",B)
print("C : ",C)

