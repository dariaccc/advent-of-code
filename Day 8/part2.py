import math

with open("Day 8/input2.txt", "r") as file:
    input = [line.strip() for line in file]

start = 0
distances = dict()
print(len(input))

for idx_i, i in enumerate(input[:len(input)-1:]):
    elements = []
    for element in i.split(","):
        elements.append(int(element))
    
    for idx_j, j in enumerate(input[start::]):
        if i != j:
            elements_j = []
            for element_j in j.split(","):
                elements_j.append(int(element_j))

            dist = math.sqrt((elements[0] - elements_j[0])**2 + (elements[1] - elements_j[1])**2 + (elements[2] - elements_j[2])**2)
            current_boxes = [i, j]
            distances[dist] = (current_boxes)

    start += 1

sort_dist = sorted(distances.items())
print(sort_dist)

print(len(distances))

# print(distances)
# all_keys = distances.keys()
# all_keys = list(all_keys)
# last_item_idx = len(all_keys) -1
# final_key = all_keys[last_item_idx]
# print(distances[final_key])