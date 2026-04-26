li=["APPLE",True,25,29.5,None,"Rabbani","The king"]
li.append("hey hello")
print(li)
li1=[5,4,3,2,1,100,10000]
li1.sort()
print("The list in the sorted manner is:\n",li1)
li.reverse()  # reversing the index values and printing them
print(li)
# Using the insert method
li1.insert(0,12)  # insert 12 at index 0 at li1
print(li1)  
li1.remove(12)   # removing 12 from li1
print(li1)
li1.pop(0)  # pop the element at index 0 from li1
print(li1)
print("Hello world !!")