marks ={
    "harry":67,
    "rabbani":100,
    "shubam":29,
#     "li":[1,23],
#     "tuple":(1,2,3),
#     "string":"rabbani"
}
print(marks.keys())
# print(marks.items())
print(marks.values())
marks.update({"harry": 99})
marks.update({"Renuka": 100})
print(marks)
# get method is used to get the values of the keys
print("The marks of the rabbani is :\n",marks.get("harry1"))  # prints none
print(marks["harry1"])  # Returns the error