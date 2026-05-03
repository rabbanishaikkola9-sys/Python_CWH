# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
# marks=int(input("Enter the marks of the student:\n"))
# if(marks>90 and marks<=100):
#     print("your grade is Ex")
# elif(marks>80 and marks<=90):
#     print("Your grade is A")
# elif(marks>70 and marks<=80):
#     print("Your grade is B")
# elif(marks>60 and marks<=70):
#     print("Your grade is C")
# elif(marks>50 and marks <=60):
#     print("Your grade is D")
# else:
#     print("Your grade is F ")
#     print("Sorry you are failed better luck next time")
# print("Results succesfully shown")
#  or you can write like 
marks=int(input("Enter the marks of the student:\n"))
if(marks>=90 and marks<=100):
    grade="Ex"
elif(marks>=80 and marks<90):
    grade="A"
elif(marks>=70 and marks<80):
    grade="B"
elif(marks>=60 and marks<70):
    grade="C"
elif(marks>=50 and marks<60):
    grade="D"
else:
    grade="F"
print(f"Your grade is {grade}")

