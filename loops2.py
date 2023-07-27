# program to print welcome a person

'''name=str(input("enter your name"))
food=str(input("enter your favorite food "))
print("hi ", name , '!nice to meet you. would you like to eat ', food,'?')'''

# this progrmas print the squares from lower limit to higher limit

def squared_series (a,b):
    for i in range(a,b):
        print("the square of number",i , "is", i*i)

n1=int(input("enter the first num"))
n2=int(input("enter the second num"))
squared_series(n1,n2)