
with open("Day 5/input2.txt", "r") as file:
    input = [line.strip() for line in file]

ranges = []
ids = []

breakpoint = input.index("")
print(breakpoint)

for idx,i in enumerate(input):

    if idx > breakpoint:
        ids.append(i)
    elif idx < breakpoint:
        ranges.append(i)

print(ranges)
print(ids)

#split the input into 2, the first with the ID ranges, then separated by a space, the IDS

#loop through id's and check if they are in any of the ranges
#how to loop through ranges?