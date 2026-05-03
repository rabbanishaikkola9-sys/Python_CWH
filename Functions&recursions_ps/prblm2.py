def f_to_c(f):
    return 5*(f-32)/9
    # print(c)


f=int(input("Enter the number in F"))
print(f"{round(f_to_c(f))}° C")

# 1. Define the Celsius value
celsius = int(input("Enter the number in celsius"))
def c_to_f(celsius):
# 2. Apply the conversion formula
    return  (celsius * 1.8) + 32

# 3. Print the result
print(f"{celsius} degrees Celsius is {round(c_to_f(celsius))}° Fahrenheit")
