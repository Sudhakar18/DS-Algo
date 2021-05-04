# Selection Sort
# Swapping the lowest element starting from the 0th element


def Selection_Sort(A):
    for i in range(0, len(A)):
        low = i
        for j in range(i + 1, len(A)):
            if A[j] < A[low]:
                low = j
        temp = A[i]
        A[i] = A[low]
        A[low] = temp
    return A


A = [5, 2, 4, 6, 1, 3]
A = Selection_Sort(A)
print(A)
