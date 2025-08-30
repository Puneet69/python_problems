a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c=int(input("Enter one more number: "))
d=int(input("Enter the last number: "))
if(a>b and a>c and a>d):
    print(a, "is the greatest")
elif(b>a and b>c and b>d):
    print(b, "is the greatest")
elif(c>a and c>b and c>d):
    print(c, "is the greatest") 
else:
    print(d, "is the greatest")
