year = int(input("which year do you want to check? "))
if (year % 4 == 0) and (year % 100 != 0):
    print("Leap year ")
elif (year % 400 == 0) and (year % 100 ==0):
    print("leap year ")
else:
    print("not a leap year ")