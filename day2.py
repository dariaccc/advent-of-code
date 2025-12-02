
with open("Day 2/input.txt", "r") as file:
    for line in file:
        input = line.split(",")

lower_bound, upper_bound = [], []

for num_range in input:
    lower_temp, upper_temp = num_range.split("-", 1)
    lower_bound.append(int(lower_temp))
    upper_bound.append(int(upper_temp))

#print(input)
#print("lower bound: ", lower_bound)
#print("upper bound: ", upper_bound)

invalid_id = []
invalid_id_sum = 0

for i in range(len(input)):
    id = lower_bound[i]
    max = len(str(upper_bound[i]))
    rep = 0
    ids = []

    if max % 2 == 0 or id % 2 == 0:
        rep = int(max/2)
    else:
      #  print("skip")
        continue

    #print(rep)

    #half = ""
    #for j in range(rep):
     #   half += (str(id)[j])

    #inv = half + half
    #print("inv ", inv)

    for id in range(lower_bound[i], upper_bound[i]):

        first_half = ""
        second_half = ""

        if (len(str(id)) % 2 == 0):
            for x in range(0, rep):
                first_half += str(id)[x]

            for y in range(rep, 2*rep):
                second_half += str(id)[y]
            
            #print(second_half)

            if first_half == second_half:
               # print("equal")
                invalid_id.append(id)
                invalid_id_sum += id
        id += 1
#    print("next ", invalid_id)

print(invalid_id)
print(invalid_id_sum)
