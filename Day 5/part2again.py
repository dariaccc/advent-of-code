
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

# for idx_i, LR_i in enumerate(lower_ranges):
#     break_loop = False
#     temp_counter = 0
#     print("i-lower is: ", LR_i)
#     print("i-upper is: ", upper_ranges[idx_i])
#     for idx_j, LR_j in enumerate(lower_ranges[:idx_i:]):

#         print("and j is: ", LR_j)
#         if (upper_ranges[idx_i] < LR_j) or (LR_i > upper_ranges[idx_j]):
#             temp_counter = upper_ranges[idx_i] - LR_i + 1
#         elif LR_i >= LR_j and upper_ranges[idx_i] <= upper_ranges[idx_j]:
#             temp_counter = 0
#         elif upper_ranges[idx_i] < upper_ranges[idx_j] and LR_i < LR_j:
#             temp_counter = LR_j - LR_i
#             upper_ranges[idx_i] = LR_j
#         elif upper_ranges[idx_i] > upper_ranges[idx_j] and LR_i > LR_j:
#             temp_counter = upper_ranges[idx_i] - upper_ranges[idx_j]
#             LR_i = upper_ranges[idx_j] + 1
#         elif upper_ranges[idx_i] > upper_ranges[idx_j] and LR_i < LR_j:
#             #temp_counter = upper_ranges[idx_i] - upper_ranges[idx_j] + LR_j - LR_i
#             #print("test here. ", upper_ranges[idx_i] - upper_ranges[idx_j] + LR_j - LR_i)
#             #temp_counter -= upper_ranges[idx_j] - LR_j
#             print("breaking")
#             lower_ranges.append(LR_i)
#             upper_ranges.append(LR_j - 1)

#             lower_ranges.append(upper_ranges[idx_j] + 1)
#             upper_ranges.append(upper_ranges[idx_i])

#             lower_ranges.pop(idx_i)
#             upper_ranges.pop(idx_i)

#             temp_counter = 0
#             break_loop = True
#             break
        
#         if break_loop: break

#     #if break_loop:
        
#     print(temp_counter)
#     counter += temp_counter

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
            elif LR_i >= LR_j and upper_ranges[idx_i] <= upper_ranges[idx_j]: #if INSIDE - <------ISSUE
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
            
#first try, second try: 432862835533246 <-----too high!
#third try: 434545676704227 <-------- definitely, definitely too high!
#fourth try: 426747832457279
#fifth try: 383342346457340 <--------- still much too high
#6: 359526404143208


#when the loop breaks, it skips one iteration of i - while loop is the solution