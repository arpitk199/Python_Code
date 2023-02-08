myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
print(myList)

# Duplicate value 
myList1 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
print(myList1)

# List Length
# To determine how many items a list has, use the len() function:
myList2 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
print(len(myList1))

# A list can contain different data types:
list1 = ["abc", 34, True, 40, "male"]
print(list1)

# What is the data type of a list?
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))

# Access Items
# List items are access them by referring to the index number:

myList1 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
print(myList1[0])
print(myList1[1])
print(myList1[2])
print(myList1[3])
print(myList1[4])
print(myList1[5])

# Negative Indexing
myList1 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
print(myList1[-1])
print(myList1[-2])
print(myList1[-3])
print(myList1[-4])
print(myList1[-5])

# slicing in list 
myList1 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
print(myList1[1:3])
print(myList1[1:5])
print(myList1[1::2])
print(myList1[-6:-1])


# Change List Items
# To change the value of a specific item, refer to the index number:
myList1 = ["Apple", "Orange", "Banana", "Apple", "Kiwi", "Graps"]
myList1[1]="Cherry"
print(myList1)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# Insert Items
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("Amit")
print(thislist)

# Extend List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# Remove list items from the list 
# The remove() method removes the specified item.
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.remove("Apple")
print(myList)

# Remove Specified Index
# The pop() method removes the specified index
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.pop(1)
print(myList)

# If you do not specify the index, the pop() method removes the last item.
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.pop()
print(myList)

# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# The clear() method empties the list
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.clear()
print(myList)

# Sort Lists
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.sort()
print(myList)

# Sort the list numerically:
list2=[75, 65, 1.0, 100, 80, 90]
list2.sort()
print(list2)

# Sort Descending
# To sort descending, use the keyword argument reverse = True:
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.sort(reverse=True)
print(myList)

# Sort the list descending
list2=[75, 65, 1.0, 100, 80, 90]
list2.sort(reverse=True)
print(list2)

# Reverse Order
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myList.reverse()
print(myList)

# Copy a List
# There are ways to make a copy, one way is to use the built-in List method copy().
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myListt=myList.copy()
print("myListt",myListt)

# Another way to make a copy is to use the built-in method list().
myList = ["Apple", "Orange", "Banana", "Kiwi", "Graps"]
myListt1=list(myList)
print("myListt1", myListt1)