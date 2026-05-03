# 3. Write a program to print multiplication table of a given number using for loop. using while loop
num=int(input("Enter the number to be multiplied:\n"))
i=1
while(i<=10):
    print(f"{num} X {i} = {num*i}")
    i+=1