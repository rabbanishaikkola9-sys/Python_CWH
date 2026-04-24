# . Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
words={
    "kela":"banana",
    "kaise ho":"how are you?",
    "kon ho":"who are you"
}
word=input("Enter the key of the dictionary")
print(words[word])
# print(words,type(words))
# print(len(words))  # depends on how many items are in the dictionary