height = input("what is your height: ")
weight = input("what is your weight: ")
BMI = int(weight) / float(height) ** 2
BMI_result = int(BMI)
print(f"Your BMI is {BMI_result}")