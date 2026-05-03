# 6. Write a python function which converts inches to cms.
def inch_to_cm(inch):
    return inch*2.54
n=int(input("Enter the value in inches:\n"))
print(f" The inch {n} in CM is :{inch_to_cm(n)}")