# list=[]
# list.append(input("Enter a word to check its palindrome or not: "))
# list.append(input("Enter another word to check its palindrome or not: "))
# list.append(input("Enter another word to check its palindrome or not: "))
# list.append(input("Enter another word to check its palindrome or not: "))
# for l in list:
#     if l==l[::-1]:
#         print(l,"is a palindrome")
#     else:
#         print(l,"is not a palindrome")
list1=[1,2,3,4,5,6]
list2=[1,4,5,5,4,1]
copy_list1=list1.copy()
copy_list2=list2.copy()
copy_list1.reverse()
copy_list2.reverse()
if list1==copy_list1:
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
if list2==copy_list2:
    print("list2 is a palindrome")
else:
    print("list2 is not a palindrome")