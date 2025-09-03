# def sum_of_natural_numbers(n):
#     if n == 1:
#         return 1
#     else:
#         return n + sum_of_natural_numbers(n-1)

# sum = sum_of_natural_numbers(5)
# print("The sum of first 5 natural numbers is:", sum)

def print_list(list , index):

    print(list[index])
    if index + 1 < len(list):
        print_list(list, index + 1)

list = ["apple", "banana", "cherry"]
print_list(list, 0)