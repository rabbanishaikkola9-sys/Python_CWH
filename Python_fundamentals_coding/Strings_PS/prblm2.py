# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''
name=input("Enter the username:\n")
print("Dear " ,name,"\n You are selected!\n","22/04/2026")  
# Can also use the f strings
print(f"Good afternoon {name}\n You are selected \n 22/04/2026")
print("End of the program:....")
#  we can use it like this 
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
print(letter.replace ("<|Name",name).replace("<|Date|>","22/04/2026"))