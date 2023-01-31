# 1. WAP to concatinate to list a [1,2,3,4,] list b [5,6,7,8]

a = [1,2,3,4,]
b = [5,6,7,8]
print(a+b)

# 2. WAP to slice on [1,'kishna',10.0,0j (4+2j)] get value [10.0,0j]

myList=[1,'kishna',10.0,0j,(4+2j)]
print(myList[2:4])

# 3. WAP to convert string A to Z convert into small letter

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet.lower())

# 4. WAP to convert a string a = NnkriShna714@Gmail.com ino lower case withaut using lower() method

a = "NnkriShna714@Gmail.com"
print(a.casefold())

# 5. wap to remove spaces given in a string a="    NnkiShna714@gmail.com     "

a="    NnkiShna714@gmail.com     "
print(a.strip())

# 6.wap Two program to get this result
# 	c="krishna"
# 	d="kumar"
# 	Result: krishnakumar
c="krishna"
d="kumar"
print(c+d)

e=c+d
print(e)

f="".join([c,d])
print(f)

# 7.wap to get 
# 	c="krishna     "
# 	d="    kumar"
# 	Result: krishnakumar 

f="krishna    "
g="    kumar"
print(f.rstrip(),g.lstrip())


