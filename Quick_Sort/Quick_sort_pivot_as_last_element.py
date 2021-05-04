def Quick_Sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        Quick_Sort(A, p, q - 1)
        Quick_Sort(A, q + 1, r)


def partition(A, p, r):
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i = i + 1
            # swap(A[i],A[j])
            A[i],A[j] = A[j],A[i]
    #swap(A[i + 1], A[r])
    A[i+1],A[r]=A[r],A[i+1]
    return i + 1

A = [2, 8, 7, 1, 3, 5, 6, 4]
p = 0
r = len(A) - 1
Quick_Sort(A, p, r)
print(A)
