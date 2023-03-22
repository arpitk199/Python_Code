# for i in range(5):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")

# for i in range(5):
#     for j in range(0,i+1):
#         print(i,end="")
#     print("")

# for i in range(0,7):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print("")

# # revers pattern

# for i in range(7,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()


# a=[0,1,2,3,4,5,6,7,8,9]
# for i in a:
#     if (i%2) == 0:
#         print(i)

# a=[i for i in range(10) if (i%2 == 0) ]
# print(a)


a=[1,2,3,4]
b=["krishna","Rohan","Sohan","Ranvir"]
c=["Kumar","Agrwal","Malhotra","Kapoor"]

for i,j,k in zip(a,b,c):
    print(i,j,k, sep=",")