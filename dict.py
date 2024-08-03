#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#Have key and values
#Written : {}

#Declare an empty dict
d1 = {}
#Another Way => d1 = dict()

d2 = {
  "name": "Priya",
  "surname": "Shah",
  "year": 2004
}

print(d2["name"])

for i in range(5):
	key = input("Enter key : ")
	val = input("Enter value : ")
	d1[key] = val
print(d1)

#Length snd type of dict
print(len(d2))
print(type(d2))

d3 = dict(science = 19, maths = 20, english = 17, hindi = 17, grammer = 16)
print(d3)

#Get value from key
print(d3["maths"])
val = d3.get("maths")
print(val)

#Get keys from dict
keys = d3.keys()
print(keys)

#Get values from dict
val = d3.values()
print(val)

#Get keys,values from dict as tuple
t1 = d3.items()
print(t1)

if "grammer" in d3:
  print("Yes, 'grammer' is one of the keys in the marks dictionary")

print("Minimum value:", min(d3.values()))
print("Maximum value:", max(d3.values()))
print("Minimum value:", min(d3.keys()))
print("Maximum value:", max(d3.keys()))

#Update value in dict
print(d3)
d3.update({"maths": 19})
print(d3)

#Loops in dict
for x in d3:
	print(x)

for x in d3:
	print(d3[x])

for x in d3.values():
	print(x)

for x in d3.keys():
	print(x)

for x, y in d3.items():
  print(x, y)

#Copy dict
d4 = d3.copy()
d5 = dict(d3)

#Remove items from dict
d3.pop("hindi")
d3.popitem() #Last item removed
del d3["english"]
d3.clear() #Dict is emptied
print(d3)