height = float(input("what is your height in m: "))
weight = float(input("what is your weight in kg: "))
BMI =   round(float(weight / height ** 2),2)
if BMI <= 18.5:
    print("you are underweight ")
    if BMI >= 18.5:
        print("you have a normal weight ")
    elif BMI <= 25:
        print("you have a normal weight ")
    if BMI >=25:
        print("you are overweight ")
    elif BMI <=30:
        print("you are overweight ")
    if BMI >= 30:
        print("you are obese")
    elif BMI <=35:
        print("you are obese")
    if BMI >= 35:
        print("you are clinically obese ")
