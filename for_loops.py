# list=[]
# for i in range(1, 11):
#     print(i*i)
#     list.append(i*i)
# print("The list of squares is:", list)
# tuple = tuple(list)
# print("The tuple of squares is:", tuple)
# x=int(input("Enter a number to check if it is in the tuple: "))
# if x in tuple:
#     print(x, "is in the tuple.")
# else:
#     print(x, "is not in the tuple.")
# num=int(input("Enter a number to check if it is in the tuple using for loop: "))
# for i in tuple:
#     if i == num:
#         print(num, "is in the tuple.")
#         break
# else:
#     print(num, "is not in the tuple.")

for i in range(100):
    print(i+1)
    i += 1

for i in range(100, 0, -1):
    print(i)

n=int(input("Enter a number: "))
for i in range(1, 11):
    print(n, "*", i, "=", n*i)
