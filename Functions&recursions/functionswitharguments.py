def goodday(name,ending):
    print("Good day",name)
    print(ending)
# goodday("harry")
goodday("harry","Thank you")
goodday("Divya","Thanks darling!!")
goodday("rabbani","Thank you")
# Using the return value

def return_value(name):
    print("Good boy",name)
    return "done"
n=return_value("Rabbani")
print(n)
n=return_value("Rohan")
print(n)