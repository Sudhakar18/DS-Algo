# Radix Sort
# uses Counting Sort
# Stable Sort

def Counting_Sort(A, place):
    C = [0] * 10
    B = [0] * len(A)
    for i in range(0, len(A)):
        index = A[i] // place
        C[index % 10] += 1
    for j in range(1, len(C)):
        C[j] = C[j] + C[j - 1]
    for i in range(len(A) - 1, -1, -1):
        index = A[i] // place
        B[C[index % 10] - 1] = A[i]
        C[index % 10] -= 1
    for j in range(0, len(A)):
        A[j] = B[j]


def Radix_Sort(A):
    maxx = max(A)
    place = 1
    while maxx // place > 0:
        Counting_Sort(A, place)
        place *= 10
    return A


A = [329, 45, 657, 8, 436, 1254, 72, 3, 0]
res = Radix_Sort(A)
print(res)
