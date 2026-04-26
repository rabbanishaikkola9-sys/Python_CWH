# 6. Write a program to calculate the factorial of a given number using for loop.
n=int(input("Enter the number that you wanna find the factorial:\n"))
result=1
# Example for this is :
# 5!= 5 X 4 X 3 X 2 X 1 
for i in range(1,n+1):
    result=result*i
    i-=1
print(result)