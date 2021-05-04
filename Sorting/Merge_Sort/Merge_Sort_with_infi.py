import math as math


def Merge(A,p,q,r):
    n1=q-p+1
    n2=r-q
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=A[p+i]
    for j in range(n2):
        R[j] = A[q+j+1]
    L.append(math.inf)
    R.append(math.inf)
    i=0
    j=0
    for k in range(p,r+1):
        if L[i]<R[j]:
            A[k] = L[i]
            i = i+1
        else:
            A[k] = R[j]
            j=j+1


def Merge_Sort(A,p,r):
    if p<r:
        q = math.floor((p+(r-1))/2)
        Merge_Sort(A,p,q)
        Merge_Sort(A,q+1,r)
        Merge(A,p,q,r)
A = [2,4,5,7,1,2,3,6]
p=0
r=len(A)-1
Merge_Sort(A,p,r)
print(A)