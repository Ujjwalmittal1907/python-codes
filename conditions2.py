def grade_system(marks) :
    if marks > 90:
        print("well done\nyou passed with AA grade")
    elif marks>80:
        print("very good\n you passed with AB grade")
    elif marks>70:
        print ("good\n you passed with B grade")
    elif marks>60:
        print("you passed with C grade")
    elif marks>33:
        print("you passed with D grade")
    else:
        print("you are FAIL")

marks=int(input("enter your score:"))
grade_system(marks)
