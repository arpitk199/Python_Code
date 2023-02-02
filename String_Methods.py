# Strings are immutable

a = "Amit"
print(len(a))
print(a.upper())
print(a.lower())
print(a.casefold())
print(a.count("Amit"))
print(a.capitalize())

str1 = "Welcome to the Jungle !!"
print(str1.endswith("!!"))

str2 = "Welcome to the Jungle !!"
print(str2.endswith("to", 4, 10))

Str3 = "My name is Arpit Kumar"
print(Str3.find("is"))

str4 = "MyNmaeisArpit"
print(str4.isalnum())

str5 = "Amit33"
print(str5.isalpha())

str6 = "amit"
print(str6.islower())

str7 = "Rajkiya Engineering College Banda"
print(str7.istitle())

str7 = "Rajkiya engineering College banda"
print(str7.title())

# using split() method convert a string into list 
myString = "My name is Arpit Kumar and i am From Kanpur Dehat"
print(myString.split())