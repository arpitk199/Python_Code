a=dict()
print(a)

b={}
print(b)

c={1: "Amit", 2: "Rahul", 3: "Shivam"}
print(c)
print(c[1])
print(len(c))
print(type(c))

# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)

d={1: "Amit", 2: "Rahul", 3: "Shivam"}
print(d.get(1))

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
e={1: "Amit", 2: "Rahul", 3: "Shivam"}
print(e.keys())

# Get Values
# The values() method will return a list of all the values in the dictionary.
f={1: "Amit", 2: "Rahul", 3: "Shivam"}
print(f.values())

# The items() method will return each item in a dictionary, as tuples in a list.
print(f.items())

# Change Values
# You can change the value of a specific item by referring to its key name:
g={1: "Amit", 2: "Rahul", 3: "Shivam"}
g[1]="Arpit"
print(g)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs
h={1: "Amit", 2: "Rahul", 3: "Shivam"}
h.update({4: "Angle"})
print(h)
h.update({2:"Karan"})
print(h)

# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name
i={1: "Amit", 2: "Rahul", 3: "Shivam"}
i.pop(1)
print(i)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
j={1: "Amit", 2: "Rahul", 3: "Shivam"}
j.popitem()
print(j)

# The clear() method empties the dictionary:
k={1: "Amit", 2: "Rahul", 3: "Shivam"}
k.clear()
print(k)

# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only 
# be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# Make a copy of a dictionary with the copy() method:
l={1: "Amit", 2: "Rahul", 3: "Shivam"}
m=l.copy()
print(m)
print(l)

