def fun(B):
    print("*****Function Starts*****")
    print(id(B))
    # 3 here still B is pointing to address of value 2 i.e. 4432929952

    B = 3
    # 4 now, python creates a new address for 3 and points it to B
    # so B will be having a new memory address i.e. 4432929984
    print(id(B))
    print("*****Function Ends*****")
    return B


B = 2
# 1 here 2 is allocated a memory location of 4432929952
print(id(B))
B = fun(B)  # 2 while the function executes the memory address of the value 2 is passed
# 5 since the function returns the address of 3, the B here is assigned with address of 3 i.e. 4432929984
print(B)
print(id(B))
