
with open("Day 5/input2.txt", "r") as file:
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
#index = 0
counter = 0
overlap = []
x = ""

min_j = lower_ranges[0]
max_j = upper_ranges[0]
ranges = []

for index, i in enumerate(lower_ranges):

    for idx_j,j in enumerate(lower_ranges[0:index:1]):
        if (lower_ranges[index] < j and upper_ranges[index] < j) or (lower_ranges[index] > j and upper_ranges[index] > j) or (len(str(j)) == 0):
            x = "not in range"
        elif lower_ranges[index] > j and upper_ranges[index] < j:
            x = "skip"
        else:
            x = "overlap"
            overlap.append(idx_j) #how to get the one it is overlapping WITH
        if j < min_j:
            min_j = j
        if j > max_j:
            max_j = j
        
    if x == "not in range":
        counter = counter + (upper_ranges[index] - lower_ranges[index]) + 1
    elif x == "skip":
        pass
    elif x == "overlap":
        print("overlap", overlap)
        for k in overlap:
            if i > lower_ranges[k] and upper_ranges[index] > upper_ranges[k]:
                #if upper_ranges[index] > max_j #what is going on here
                counter += upper_ranges[index] - upper_ranges[k]
                print("here")
            elif i < lower_ranges[k] and upper_ranges[index] < upper_ranges[k]:
                counter += lower_ranges[k] - i
            elif i < lower_ranges[k] and upper_ranges[index] > upper_ranges[k]:
                counter += (upper_ranges[index] - upper_ranges[k]) + lower_ranges[k] - i
        


# for _ in range(len(lower_ranges)):
#     for j in range(lower_ranges[index], upper_ranges[index] + 1):
#         #print(j)
#         if j not in ranges:
#             #counter += 1
#             ranges.append(j)
#     print(index)    
#     index += 1

#print(ranges)
# print(len(ranges))
print(counter)

#better way to do it --> upper_ranges[idx] - lower_range[idx]
#for all the ranges:
#if lower and upper are both smaller than all previous, add to counter
#if lower and upper are both bigger than all previous, add to counter
#if in any other range, the lower is bigger and the upper is smaller, skip completely
#if for a range the smaller is smaller, but the bigger is also smaller subtract the smaller of the lower ranges from the other and add
#if for a range the smaller is bigger, but the bigger is also bigger subtract the bigger of the upper ranges from the other and add