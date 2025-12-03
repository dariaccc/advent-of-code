

with open("Day 2/input.txt", "r") as file:
    for line in file:
        input = line.split(",")

lower_bound, upper_bound = [], []

for num_range in input:
    lower_temp, upper_temp = num_range.split("-", 1)
    lower_bound.append(int(lower_temp))
    upper_bound.append(int(upper_temp))

invalid_id = []
invalid_id_sum = 0

max_length = 0
for i in upper_bound:
    if len(str(i)) > max_length:
        max_length = len(str(i))

#print(max_length)

vars2 = []
for i in range(len(input)):
    id = lower_bound[i]
    max = len(str(upper_bound[i]))
    rep = 0
    ids = []

    for id in range(lower_bound[i], upper_bound[i] + 1):
        for div in range(2, max_length):
            cur = ""

            vars1 = []
            if(id % div == 0):
                y = int(len(str(id))/div)
                
                vars1 = []
               # print(div, y)

                for j in range(div):
                    for k in range(y):
                        cur += str(id)[k]
                if (cur != "") and (cur not in vars1):        
                    vars1.append(cur)
            if(len(vars1) != 0) and (len(cur) == len(str(id))) and (vars1 not in vars2) and (lower_bound[i] <= int(vars1[0]) <= upper_bound[i]):
                vars2.append(vars1)

        id += 1

print(len(vars2))
print(vars2)

sum = 0
for i in vars2:
    sum += int(i[0])

print(sum)

    # if(max % 2 == 0) or (len(str(id)) % 2 == 0):
    #     rep = int(max/2)
    # else:
    #     continue

    # for id in range(lower_bound[i], upper_bound[i] + 1):

    #     j = 0
    #     for _ in range(1, len(str(id))):
    #         current = str(id)[j]
    #         next = str(id)[j + 1]            

    #         #print(current, next)

    #         if current == next:
    #             invalid_id.append(id)
    #             invalid_id_sum += id
    #         j += 1

#print(invalid_id)
#print(invalid_id_sum)


# for i in range(len(input)):
#     j = 0
#     id = lower_bound[i]
#     while(id < upper_bound[i]):
#         current = 0
#         previous = 0
#         for j in range(len(str(id))):
#             current = int(str(id)[j])
#             if current == previous:
#                 invalid_id.append(id)
#             else:
#                 current = int(str(current) + str(previous))
#             j += 1
#         print(invalid_id)
#         id += 1