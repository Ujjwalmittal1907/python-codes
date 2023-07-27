# for finding the largest number among three's
def find_largest(num1,num2,num3):
    if num1>num2 & num1>num3:
        print(str(num1) + "is largest")
    elif num2 > num1 & num2>num3:
        print(str(num2) + "is largest")
    if num3>num1 & num3>num2:
        print(str(num3) , "is largest")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))
find_largest(num1,num2,num3)