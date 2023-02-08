myTuple = (1, "Amit", 1.0, [1,2,3,4])
print(myTuple)

# Access tuple and indexing
a=(1,2,3,4,5,6,7,8,9,)
print(a[3])

# Slicing in tuple 
a=(1,2,3,4,5,6,7,8,9,)
print(a[1:6])

# a=(1) #this is not tuple
# a=(1,) this is tuple 

# tuple method
a=(1,2,3,4,5,6,7,8,9,)
print(a.count(5))

print(a.index(5))

# Unpacking tuple 

tuple1 = ("Apple", "Banana", "mango", "Cherry")
red, green, yellow, blue = tuple1
print(red)
print(green)
print(blue)
print(yellow)

a = tuple((1,2,3,4,5,6))
print(type(a),a)



