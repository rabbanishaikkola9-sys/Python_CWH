import os
# Labelling the comments from prblm 
# specify directory path (you can change this)
path = "C:/"

# get contents of directory
contents = os.listdir(path)

# print each item
print("Contents of directory:")
for item in contents:
    print(item)