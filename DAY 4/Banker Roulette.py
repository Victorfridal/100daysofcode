import random

name_string = input("Give me everybody's name, seperated by a coma. ")

names = name_string.split(",")
number_items = len(names)
random_picks = random.randint(0,number_items - 1)
who_pays = names[random_picks]
print(who_pays + "will pay for the meal.")
