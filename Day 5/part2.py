
#note here
with open("Day 5/input.txt", "r") as file:
    input = [line.strip() for line in file]

lower_ranges = []
upper_ranges = []

breakpoint = input.index("")

for idx,i in enumerate(input):
    if idx < breakpoint:
        i, j = i.split("-",1)
        lower_ranges.append(int(i))
        upper_ranges.append(int(j))

print(lower_ranges, upper_ranges)

counter = upper_ranges[0] - lower_ranges[0] + 1
print(counter)

skip_list = []

for idx_i, LR_i in enumerate(lower_ranges):
    break_loop = False
    temp_counter = 0
    print("i-lower is: ", LR_i)
    print("i-upper is: ", upper_ranges[idx_i])
    for idx_j, LR_j in enumerate(lower_ranges[:idx_i:]):

        print("and j is: ", LR_j)
        if (idx_j not in skip_list):
            if (upper_ranges[idx_i] < LR_j) or (LR_i > upper_ranges[idx_j]): #if both above or below
                temp_counter = upper_ranges[idx_i] - LR_i + 1
            elif LR_i >= LR_j and upper_ranges[idx_i] <= upper_ranges[idx_j]: #if INSIDE
                temp_counter = 0
                break_loop = True
                break
            elif upper_ranges[idx_i] < upper_ranges[idx_j] and LR_i < LR_j: #if lower overlap
                temp_counter = LR_j - LR_i
                upper_ranges[idx_i] = LR_j - 1
            elif upper_ranges[idx_i] > upper_ranges[idx_j] and LR_i > LR_j: #if upper overlap
                temp_counter = upper_ranges[idx_i] - upper_ranges[idx_j]
                LR_i = upper_ranges[idx_j] + 1
            elif upper_ranges[idx_i] >= upper_ranges[idx_j] and LR_i <= LR_j: #if OUTSIDE
                print("breaking")

                if LR_i != LR_j:
                    lower_ranges.append(LR_i)
                    upper_ranges.append(LR_j - 1)

                if upper_ranges[idx_i] != upper_ranges[idx_j]:
                    lower_ranges.append(upper_ranges[idx_j] + 1)
                    upper_ranges.append(upper_ranges[idx_i])

                skip_list.append(idx_i)

                temp_counter = 0
                break_loop = True
                break
        
        if break_loop: break
        
    print(temp_counter)
    counter += temp_counter

print(lower_ranges, upper_ranges)
print("counter is: ", counter)