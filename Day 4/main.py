rolls = []
with open("Day 4/input.txt", "r") as file:
    for line in file: rolls.append(line.strip())

print(rolls) #the whole shelf of rolls

start = 0
stop = 8
forklift = 0

for idx_row, row in enumerate(rolls): #for each row of scrolls in the shelf
    
    for idx_roll,roll in enumerate(row):
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

print(forklift)




#what i need to do
#for x (the current position), if it is @:
#check idx(x) - 1, and idx(x) + 1
#if they are scrolls, add to a list
#then check the previous row for idx(x), idx(x) - 1 and idx(x) + 1
#then check the NEXT row for idx(x), idx(x) - 1 and idx(x) + 1
# if they are scrolls, add them to the list
# edge cases? if "previous" = 0, skip
# if "next" = len(rolls), skip
 