# 7. Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3
n=int(input("enter the rows of the pyramid that is full pyramid or star pattern"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    # print("*"*(n-i))
    print("*"*(2*i-1),end="")
    print(" ")  # can also use \n
print("end of the half pyramid or pattern")