groceries = [
    ['sugar', 'bread', 'milk'],
    ['tomatoes', 'pepper', 'onions', 'ginger'],
    ['yam', 'rice', 'semovita'], 
    ['apple juice', 'carrot juice', 'vinegar']]
sol = groceries[2][2]
sol1 = groceries[1][3]
sol2 = groceries[1][0]
sol3 = groceries[0][0]
print(f"{sol}\n{sol1}\n{sol2}\n{sol3}")
groceries[3][0]= "cinnamon tea"
groceries[2][2]= "poundo"

groceries.append(["curry","thyme","rosemary"])
print(groceries)
groceries[0].append("milo")
groceries[4].append("maggi")
print(groceries)
