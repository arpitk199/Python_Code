a=set()
print(a, type(a))

b={1,2,3,4,5}
print(b)
print(type(b))

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

c={1,1.2,"Amit", }
print(c)

d={(1,)}
print(d)

# e={{1}}
# print(e) TypeError: unhashable type: 'set' nesting not allowed in set


# g={[1]}
# print(g) TypeError: unhashable type: 'list'

# set lenth
this_set={1,2,3,4,6,7,8}
print(len(this_set))

# Add Items
# To add one item to a set use the add() method.
set1={"Amit","Ravi"}
set1.add("Piyush")
print(set1)

# Add Sets
# To add items from another set into the current set, use the update() method.
e={1,2,3,4,5}
f={1,2,6,7,8}
e.update(f)
print(e)

# Add Any Iterable
set2={"Apple","Mango","Bnana"}
myList=["Kiwi","Cherry"]
set2.update(myList)
print(set2)

# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
set3={"Apple","Mango","Bnana"}
set3.remove("Apple")
print(set3)

set4={"Apple","Mango","Bnana"}
set4.discard("Mango")
print(set4)

# Remove a random item by using the pop() method:
# note: array store value but other collection like list tuple set store id othe element
set5={"Apple","Mango","Bnana"}
set5.pop()
print(set5)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

# Join Two Sets
# There are several ways to join two or more sets in Python.
# You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another:
set6={"a","b","c","d"}
set7={1,2,3,4,5,6}
set8=set6.union(set7)
print(set8)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)

# The intersection_update() method will keep only the items that are present in both sets.
x={"Amit","Ravi","Piyush"}
y={"Amit","Arpit","Apple"}
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets
x={"Amit","Ravi","Piyush"}
y={"Amit","Arpit","Apple"}
z=x.intersection(y)
print(z)

p={1,3,4,5,6}
q={1,2,6,7,8,9}
print(p.intersection(q))

# Keep All, But NOT the Duplicates
# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
l = {"apple", "banana", "cherry"}
m = {"google", "microsoft", "apple"}
n=l.symmetric_difference(m)
print(n)



