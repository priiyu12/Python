#Set items are unordered, unchangeable, but you can remove items and add new items.
#Written : {}

#Declare an empty set
s2 = set()
s5 = {"abc", "off", 1, 4}
s1 = {0, "apple", "banana", "cherry", True, False, 1, "guava", "kiwi", "papaya"}
s3 = {"pink", "green", "red", "orange"}
l1 = ["grey", "purple"]
s4 = {"green", "purple", "white", "blue", "black"}
#Another way => s1 = set(("apple", "banana", "cherry")) 
print(s2)
print(s1)

#Length of set
print(len(s1))
print(len(s2))

#Type of variable  =>  class set
print(type(s1))
print(type(s2))

for x in s1:
  print(x)

#Checking presence of elemnets in sets : return boolean value
print("kiwi" in s1)
print("banana" in s1)
print("banana" not in s1)

#Adding items or updating sets
s2.add("blue")
s2.update(s3)
s2.update(l1)
print(s2)

#Removing items from sets
s1.remove("kiwi")
print(s1)
s1.discard("banana")
print(s1)
s1.discard(True)
print(s1)
x = s1.pop()
print(x, s1)

#Clearing set
print(s5)
s5.clear()
print(s5)
del s5

s5 = {"abc", "off", 1, 4}

#Set Methods
print("UNION")
print("S2 : ", s2)
print("S3 : ", s3)
print("S4 : ", s4)

print(s3.union(s4))
print(s3 | s4)

print(s3.union(s4,s2))
print(s3 | s4 | s2)

print(s3.union(l1))

s5.update(s3)
print(s5)

print("INTERSECTION")
print("S2 : ", s2)
print("S3 : ", s3)
print("S4 : ", s4)
print("S5 : ", s5)

print(s3.intersection(s4))
print(s3 & s4)

print(s4)
s4.intersection_update(s2)
print(s4)

print("DIFFERENCE")
print("S2 : ", s2)
print("S3 : ", s3)
print("S4 : ", s4)
print("S5 : ", s5)

print(s3.difference(s2))
print(s3 - s2)

s3.difference_update(s2)
print(s3)

print("SYMMETRIC DIFFERENCE")
print("S2 : ", s2)
print("S3 : ", s3)
print("S4 : ", s4)
print("S5 : ", s5)

print(s3.symmetric_difference(s4))
print(s3 ^ s4)

print(s3)
print(s4)
s3.symmetric_difference_update(s4)
print(s3)

print("RELATIONS")
print("S2 : ", s2)
print("S3 : ", s3)
print("S4 : ", s4)
print("S5 : ", s5)

print(s4.issubset(s3))
print(s3.issuperset(s2))
print(s4.isdisjoint(s5))
print(s4.isdisjoint(s2))

print("ELEMENTS OPERATIONS")
s6 = {45, 89, 7, 1, 0}
print("S6 : ", s6)
print(sorted(s6))
print(len(s6))
print(min(s6))
print(max(s6))
print(sum(s6))