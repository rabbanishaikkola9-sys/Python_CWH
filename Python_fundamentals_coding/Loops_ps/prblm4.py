# n=int(input("Enter the number that you wanna whehter is it prime or not:\n"))
# for i in range(0,n+1):
#     if((n%2)==0):
#         print(f"{n} is prime")
#     else:
#         print(f"{n} is not a prime")
# or it can written like this
n1=int(input("Enter the number that you wanna whehter is it prime or not:\n"))
for i in range(2,n1):
    if(n1%i)==0:
        print(f"{n1} is not prime")
        break
else:
    print(f"{n1} is prime")
        
