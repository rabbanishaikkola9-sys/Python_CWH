'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''
def fact_(n):
    if(n==0 or n==1):
        return 1
    return n*fact_(n-1)
n=int(input("Enter the number that you wanna find factorial:\n"))
print(f"the factorial of {n} is {fact_(n)}")