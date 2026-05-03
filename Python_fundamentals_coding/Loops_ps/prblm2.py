# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S. and also ends with y and  i.
l = ["Harry","rabbani", "Soham", "Sachin", "Rahul","Samanata"]
for i in l:
    # if(i.startswith("S")):
    #     print(i)
    if(i.endswith("y") or  i.endswith("i")):
        print(i)
    # else:
        # print(i)