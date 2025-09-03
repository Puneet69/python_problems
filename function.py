def length_of_list(list):
    return len(list)


def print_list(list):
    for item in list:
        print(item) 
    
def factorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * factorial(num-1)

def usd_to_inr(usd):
    return usd * 74.5

list = ["ram","shyam","rahul"]
print(length_of_list(list))
print_list(list)
num=int(input("Enter a number: "))
print(factorial(num))
print(usd_to_inr(num), "rupees")