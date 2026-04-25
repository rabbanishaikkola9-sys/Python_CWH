# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.
p1="click this"
p2="Make a lot of money "
p3="subscribe this"
p4="buy now"
msg=input("Enter the message:\n")
if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This comment  is spam")
else:
    print("comment is not a spam You are safe!!")