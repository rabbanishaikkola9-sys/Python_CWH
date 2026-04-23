s1={1,45,6,78}
s2={7,8,1,78}
print(s1.union(s2))  # takes all the values from both the sets but removes the duplicates
print(s1.intersection(s2))  # takes the common values from both the sets
# print(s1.clear())
# print(s1)
print({1,45}.issubset(s1))  # returns True
print(s1.issuperset({1}))  # returns True
print({1,2,3}.issubset(s2))  # returns False