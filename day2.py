
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

for i in range(len(input)):
    id = lower_bound[i]
    max = len(str(upper_bound[i]))
    rep = 0

    if id % 2:
        rep = int(max/2)
    else:
        continue

    print(rep)

    half = ""
    for j in range(rep):
        half += (str(id)[j])

    inv = half + half
    print("inv ", inv)
    
  #  if int(inv) in range(lower_bound[i], upper_bound[i]):
   #         invalid_id.append(id)
    id += 1

    #print(invalid_id)