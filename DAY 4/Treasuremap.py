row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want the treasure? ")
if position[0] == '1':
    if position[1] == '1':
        map[0][0]="x"
    elif position[1]== '2':
        map[1][0]="x"
    else:
        map[2][0]="x"
elif position[0]== '2':
    if position[1] == '1':
        map[0][1]="x"
    elif position[1]== '2':
        map[1][1]="x"
    else:
        map[2][1]="x"
else:
    if position[1] == '1':
        map[0][2]="x"
    elif position[1]== '2':
        map[1][2]="x"
    else:
        map[2][2]="x"

print(f"{map[0]}\n{map[1]}\n{map[2]}")



