
def Quick_Sort(A,p,r):
    if p<r:
        q = partition(A,p,r)
        Quick_Sort(A,p,q-1)
        Quick_Sort(A,q+1,r)


def partition(A,p,r):
    X = A[p]
    i = p
    for j in range(p+1,r+1):
        if A[j]<=X:
            i=i+1
            A[i],A[j]=A[j],A[i]
    A[i],A[p]=A[p],A[i]
    return i


A = [2, 8, 7, 1, 3, 5, 6, 4]
p = 0
r = len(A) - 1
Quick_Sort(A, p, r)
print(A)