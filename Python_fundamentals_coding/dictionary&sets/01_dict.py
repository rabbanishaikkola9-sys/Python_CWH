dict={}# this is an empty dictionary
print("The list is empty",dict)
dict={
    "rabbani":100,
    "rehaan":99,
    "key":"value"
}
print(dict,"\n",type(dict))
print(dict["key"])
print(dict.keys())
print(dict.values())
print(dict.items())
dict.update({"hello":"world"})
print(dict)
print(dict.get("rabbani"))
# print(dict.get("key1"))  # used to get the value from the key
print(dict["key"])