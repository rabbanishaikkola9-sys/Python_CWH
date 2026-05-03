a=int(input("Enter the value for a "))
b=int(input("Enter the value for b "))
c=int(input("Enter the value for c "))
def great(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
print(great(a,b,c))