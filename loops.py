# 1. program for replacing  a language

'''ujjwal = ['c','c++','java','python']

for i in range(len(ujjwal)):
    print("before language at index ", i,"is",ujjwal[i] )
    ujjwal[i]= 'javascript'
    print("after replacing language at index ", i ,"is",ujjwal[i] ) '''

# 2.  another program printing tables

'''num =int(input("enter the number"))
for i in range(1,11):
    print ("num *" , i , " =",num*i )'''

# 3 programm for addition and calculation

'''sum =0
for i in range(1,8) :
    sum=sum+i

print(sum)'''

# 4 printing the pattern

'''row=int(input("enter the no of rows"))

for i in range(1,row+1):
    print()
    for j in range(i):
   print('*' , end="")  '''

# function ehich take input of two number and give sum of their square

def square_fun (a,b):
    ans = (a*a)+(b*b)
    return ans

print("hello")
num1 = int(input("enter the first number"))
num2 = int(input("enter the first number"))
print(square_fun(num1,num2))
