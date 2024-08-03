#Declare an empty list
list1 = []
#ANOTHER WAY	=>		list1 = list()

#Creating List
#list2 = ["apple", "banana", "cherry"]
list2 = list(("apple", "banana", "cherry"))
tropical = ["mango", "pineapple", "papaya"]
t1 = ("chikoo", "litchi")

#Inserting values in list
list2.append("kiwi")
list2.insert(2, "guava")

#Extending lists
list2.extend(tropical)
list2.extend(t1)

#Input elements from user
for i in range (0,6) :
	element = int(input(f"Enter elemnet {i}: "))
	list1.append(element)

print(list1)
print(list2)

#Length of list
print(len(list1))
print(len(list2))

#To get index number
print(list2.index("guava"))

#What type is it of? => Class List
print(type(list1))
print(type(list2))

#Index search : negative starts from backwards!
print(list1[-2])
print(list2[-2])
print(list1[1:4])
print(list2[:3])
print(list1[4:])

#Sorting Lists
#Ascending
list1.sort()
print(list1)
list2.sort()
print(list2)

#Descending
list1.sort(reverse = True)
print(list1)

#Reversing the list
list1.reverse()
print(list1)

#Copying List
fruits = list2.copy()
print("Fruits : ", fruits)
num = list(list1)
print("Num : ", num)

if "Hey" in list1:
  print("Yes, 'Hey' is in the list")

#Remove item from list
list2.remove("chikoo")
list2.pop(4) #remove item at 4th index
list2.pop() #remove item from last index
print(list2)
del list1[0] #delete element at 0th index
print(list1)
del list1 #delete the whole list
list2.clear()
print(list2)





