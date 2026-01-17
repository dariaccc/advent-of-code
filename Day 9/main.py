
with open("Day 9/input.txt", "r") as file:
    input = [line.strip() for line in file]

xs, ys = [], []
#print(input)
for i in input:
    for idx, num in enumerate(i.split(",")):
        if idx % 2 == 0:
            xs.append(int(num))
        else:
            ys.append(int(num))

zipped = list(zip(xs, ys))
#print(list(zipped))

res = sorted(zipped, key=lambda x: (x[1], x[0]))
#print(res)

all_areas = []
start = 1
for value in res[:-1:]:
    #print("\n")
    x1, y1 = value[0], value[1]
    for sec_value in res[start::]:
        x2, y2 = sec_value[0], sec_value[1]
        if (x1 <= x2) and (y1 <= y2):
            #print(sec_value)
            area = (x2 - x1 + 1) * (y2 - y1 + 1)
            #print(area)
            all_areas.append(area)
    start += 1

#print(all_areas)
print(max(all_areas))