# i=1
# while i <= 100:
#     print(i)
#     i += 1

# i=100
# while i >= 1:
#     print(i)
#     i -= 1

# i=int(input("Enter a number: "))
# j=1
# while j <= 10:
#     print(i, "*", j, "=", i*j)
#     j += 1

i=1
list=[]
while i <= 10:
    print(i*i)
    list.append(i*i)
    i += 1
print("The list of squares is:", list)
tuple = tuple(list)
print("The tuple of squares is:", tuple)
x=int(input("Enter a number to check if it is in the tuple: "))
if x in tuple:
    print(x, "is in the tuple.")
else:
    print(x, "is not in the tuple.")