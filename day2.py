
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

    half = ""
    for j in range(rep):
        half += (str(id)[j])

    inv = half + half
    #print("inv ", inv)
    
    for id in range(lower_bound[i], upper_bound[i]):
        if id == int(inv):
            invalid_id.append(id)
            invalid_id_sum += id
        id += 1

print(invalid_id)
print(invalid_id_sum)

#edge cases not dealth with - if the lower bound is even, that one needs to be accounted for invalid id, otherwise the upper bound
#what happens for the lowest and highest numbers?