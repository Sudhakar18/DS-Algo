# Inserion Sort
# in plcae sorting
# using of key
# O(n^2)


def insertion_sort(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j != -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    A = [5, 3, 2, 1]


A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print(A)
