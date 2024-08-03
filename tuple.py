#A tuple is a collection which is ordered and unchangeable.
#Written : ()

#Declare an empty tuple
t1 = ()
#ANOTHER WAY	=>		t1 = tuple()

#Taking user input
l1 = list(t1)
element = input("Enter element : ")
l1.append(element)
t1 = tuple(l1)

#Creating List
#t2 = ("apple", "banana", "cherry")
t2 = tuple(("apple", "banana", "cherry"))
tropical = ("mango", "pineapple", "papaya")

#Joining tuple
t3 = t1 + tropical
t4 = t1 * 3

print("T1 : ",t1)
print("T2 : ",t2)
print("T3 : ",t3)
print("T4 : ",t4)

#Counting number of repetition of elements
print(t4.count("apple"))

#Finding the index of 1st occurence of value in tuple
print(t4.index("apple"))

#Index search : negative starts from backwards!
print(t3[-2])
print(t2[-2])
print(t3[1:4])
print(t2[:3])
print(t3[1:])

#Traverse through tuple
for x in t3:
  print(x)

#Check if item exists in tuple : returns boolean value
if "apple" in t2:
	print("Yes, 'apple' is in the fruits tuple")
if "apple" in t1:
	print("Yes, 'apple' is in the fruits tuple")
else:
	print("No, 'apple' is not in the fruits tuple")

#To perform any action convert tuple to list and operate
y = list(t2)
y.remove("apple")
t2 = tuple(y)
del t2 #tuple is deleted

#functions used by tuple
t5 = (34, 6, 98, 0, 45, 1)
t6 = (22, 63, 2, 5, 1)

#Length of tuple
print(len(t5))
print(len(t6))

#Maximum of tuple
print(max(t5))
print(max(t6))

#Minimum of tuple
print(min(t5))
print(min(t6))

#Sum of tuple
print(sum(t5))
print(sum(t6))

#Sort the tuple
print(sorted(t5))
print(sorted(t6))

#Check if any one value is true? or not
print(any(t5))
print(any(t6))

#Check if all the values are true? or not
print(all(t5))
print(all(t6))

#Return values of tuple with index using enumerate
for index, value in enumerate(t5):
    print(index, value)