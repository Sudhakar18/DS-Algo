# Counting Sort
# 2 Extra arrays
# Stable Sort

def Counting_Sort(A):
    k = max(A)
    C = [0] * (k + 1)
    for i in range(0, len(A)):
        C[A[i]] = C[A[i]] + 1
    for j in range(1, len(C)):
        C[j] = C[j] + C[j - 1]
    B = [0] * len(A)
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B


A = [2, 5, 3, 0, 2, 3, 0, 3]
Sorted_A = Counting_Sort(A)
print(Sorted_A)
