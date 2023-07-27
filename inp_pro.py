def age_status(age):
    if age < 12:
        print("you are a child")
    elif age < 18:
        print("you are a teenager")
    else:
        print("you are a adult")


age=int(input("enter your age:"))
age_status(age)