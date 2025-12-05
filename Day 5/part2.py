
with open("Day 5/input.txt", "r") as file:
    input = [line.strip() for line in file]

lower_ranges = []
upper_ranges = []
ids = []

breakpoint = input.index("")
#print(breakpoint)

for idx,i in enumerate(input):
    if idx > breakpoint:
        ids.append(i)
    elif idx < breakpoint:
        i, j = i.split("-",1)
        lower_ranges.append(int(i))
        upper_ranges.append(int(j))

#print(lower_ranges, upper_ranges)
index = 0
counter = 0

ranges = []

for _ in range(len(lower_ranges)):
    for j in range(lower_ranges[index], upper_ranges[index] + 1):
        #print(j)
        if j not in ranges:
            counter += 1
            #ranges.append(j)
    print(index)    
    index += 1

print(ranges)
print(len(ranges))

#better way to do it --> upper_ranges[idx] - lower_range[idx]
#how to handle duplicates here?