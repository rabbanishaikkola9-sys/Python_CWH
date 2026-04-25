# 7. Write a program to find out whether a given post is talking about “Harry” or no
post="harry is a good boy he is waste sometime as of teaching the mechanical"
if(("Harry" in post)):  # case sensitive
    print(post,type(post))
else:
    print("Not present")