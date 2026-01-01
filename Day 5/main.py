
with open("Day 5/input.txt", "r") as file:
    input = [line.strip() for line in file]

lower_ranges = []
upper_ranges = []
ids = []

breakpoint = input.index("")
print(breakpoint)

for idx,i in enumerate(input):
    if idx > breakpoint:
        ids.append(i)
    elif idx < breakpoint:
        i, j = i.split("-",1)
        lower_ranges.append(int(i))
        upper_ranges.append(int(j))

print(ids)

fresh = 0
for id in ids:
    id = int(id)
    for index in range(len(lower_ranges)):
        if id in range(lower_ranges[index], upper_ranges[index]):
            fresh += 1
            break

print(fresh)