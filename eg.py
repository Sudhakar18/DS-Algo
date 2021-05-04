def insertion_sort(A):
    print("****inside function")
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j != -1 and A[j] > key:
            A[j + 1] = A[j]
            j = j - 1
        A[j + 1] = key
    # now instead of modifing the list, what if we allocate a new list to A
    A = [9, 9, 9, 9]
    print(A)
    print(id(A))


A = [5, 2, 4, 6, 1, 3]
insertion_sort(A)
print("****ootside function")
#the changes inside the function are not reflected here.
print(A)
print(id(A))
