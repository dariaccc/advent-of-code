#note here
rolls = []
with open("Day 4/input.txt", "r") as file:
    for line in file: rolls.append(line.strip())

print(rolls) #the whole shelf of rolls

start = 0
stop = 8
forklift = 0
new_list = []
boo = True

while boo:

    new_list = []
    for idx_row, row in enumerate(rolls): #for each row of scrolls in the shelf
        new_row = []

        for idx_roll,roll in enumerate(row): #for each roll in the row
            x = 0
            if roll == "@":
                if idx_roll - 1 < 0:
                    pass
                else:
                    if row[idx_roll - 1] == "@":
                        x += 1

                if idx_roll + 1 >= len(row):
                    pass
                else:
                    if row[idx_roll + 1] == "@":
                        x += 1

                if idx_row == 0:
                    pass
                else:
                    for idx_j, j in enumerate(rolls[idx_row - 1]):
                        if (idx_j == idx_roll - 1 or idx_j == idx_roll or idx_j == idx_roll + 1) and j == "@":
                            x += 1

                if idx_row + 1 >= len(rolls):
                    pass
                else:
                    for idx_j, j in enumerate(rolls[idx_row + 1]):
                        if (idx_j == idx_roll - 1 or idx_j == idx_roll or idx_j == idx_roll + 1) and j == "@":
                            x += 1

                if x < 4:
                    forklift += 1
                    new_row.append("x")
                else:
                    new_row.append(roll)
            elif roll == "x":
                new_row.append(".")
            else:
                new_row.append(roll)

        new_row = "".join(new_row)
        new_list.append(new_row)

    if rolls == new_list:
        print("equal!")
        break
    else:
        rolls = new_list

print(forklift)
 