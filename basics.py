 #                                 CONCEPT1
# variables in python

#its doesnot require any type of command to declare a variable
# x=5
# y='name'
# print(x)
# print(y)


# for finding the data type
# print(type(x))
# print(type(y))

#assign multiple value in one line
# x,y,z='hello','how','are'
# print(x)
# print(y)
# print(z)


#assign same value to multiple variable
# a = b = c = 'string'
#  print(a)
#  print(b)
#  print(c)


#function ke inside variable local hai and bahar global hoga .Agar hume function ke inside ke variable ko global
#banana hai then we declare it with  "global" keyword

# y = "india"                      # here it acts as global
# def firstfun():
#      y ="america"                # here y is local
#      print(y + "is world power")
#
# firstfun()                       // america is world power
# print(y + "is world power")         # india is world power



# to make local varible global in function
# y = "india"                      # here it acts as global
# def firstfun():
#      global y
#      y ="america"                # here y is local
#      print(y + "is world power")
#
# firstfun()                       # america is world power
# print(y + "is world power")         # america is world power


#                                  CONCEPT 2
# lets do if elif and else

# x=20
# y=30
# if x>y:
#    print("x is greater")
# elif x==y:
#    print("both are equal")
# else:
#     print("y is greater")

#                               CONCEPT 3(LOOPS)

#  1. while loop

# i=1
# while i<6:
#  print(i)
#  i+=1
# else:
#  print("i is no longer less than 6")

i=0
while i<=8:
 i += 1
 if i==4:
  continue
 elif i==7:
  break
 else:
  print("this is", i, "loop")


#2. FOR LOOP









