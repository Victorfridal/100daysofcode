row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do you want the treasure? ")

row = int(position[0])
column = int(position[1])

selected_row = map[row - 1]
selected_row[column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")