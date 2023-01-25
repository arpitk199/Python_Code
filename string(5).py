#Important Point about String
# String Construct is str()
# a=str()
# print(a)

a="Amit"
print(a)

b = ""
print(type(b))

c = ''
print(type(c))

d = ''''''
print(type(d))

f = """"""
print(type(f))
# String is a set of sequence of element
g = "Amit Kumar"
print(g[6])

# string support indexing
# String support slicing
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(0, 8, 1)
print(a[x])

# reversing words in a given string

string = "Amit Kumar"
s = string.split()[::-1]
print(s)

# Revers Charecter
g = "Amit Kumar"[::-1]
print(g)