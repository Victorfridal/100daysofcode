height = float(input("what is your height in m: "))
weight = float(input("what is your weight in kg: "))
BMI = round(float(weight / height ** 2),0)
print(BMI)
if BMI < 18.5:
    print(f"your BMI is {BMI}, you are underweight ")
elif BMI < 25:
    print(f"your BMI is {BMI}, you have a normal weight ")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are overweight ")
elif BMI < 35:
    print(f"your BMI is {BMI}, you are obese ")
else:
    print(f"your BMI is {BMI}, you are clinically obese ")