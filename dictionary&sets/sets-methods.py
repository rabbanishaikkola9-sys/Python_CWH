my_set={11,22,11,22,1,2,3,4,5}
print(my_set,type(my_set))
s1={1,2,3,4}
s2={1,2,4,5,6}
print(s1.union(s2)) # removes duplicate and prints all the values
print(s1.intersection(s2)) # filters the elements and choose the common elements in both the sets
print({1,2,5}.issubset(s1))  # the elements with in the sets are subset of set
print("Printing the empty set")
empty_set=set()
print(empty_set,type(empty_set))

