import math
import tqdm

with open("Day 8/input.txt", "r") as file:
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

total_con = len(distances)

all_circuits = []

for _ in tqdm.tqdm(range(total_con)):
    min_dist = min(distances)
    boxes = distances[min_dist]
    distances.pop(min_dist)

    all_circuits.append(boxes)

with open("Day 8/output.txt", "w") as f:
    print(all_circuits, file=f)

print(all_circuits)
print(len(all_circuits))

start = 1
stop_loop = 0

n = len(all_circuits) - 1
pbar = tqdm(total=n)

while stop_loop < n:
    broken = False
    circuit = all_circuits[stop_loop]

    for circ_index, sec_circuit in enumerate(all_circuits[start::]):

        if sec_circuit[0] in all_circuits[circ_index] and sec_circuit[1] not in all_circuits[circ_index]:
            last_circ = sec_circuit[1]
        elif sec_circuit[1] in all_circuits[circ_index] and sec_circuit[0] not in all_circuits[circ_index]:
            last_circ = sec_circuit[0]

        if bool(set(circuit) & set(sec_circuit)) and circuit != sec_circuit:
            all_circuits[stop_loop] = all_circuits[stop_loop] + sec_circuit
            all_circuits.remove(sec_circuit)

            broken = True
            break
    
    if broken:
        pass
    else:
        stop_loop += 1
        start += 1 
    
    pbar.update(stop_loop - pbar.n)
pbar.update(n - pbar.n)
pbar.close()

print("last box is: ", last_circ)

last_distances = dict()
last_c_elements = []

for l_element in last_circ.split(","):
    last_c_elements.append(int(l_element))

for idx_jl, jl in enumerate(input):
    if last_circ != jl:
        elements_j = []
        for element_j in jl.split(","):
            elements_j.append(int(element_j))

        dist = math.sqrt((last_c_elements[0] - elements_j[0])**2 + (last_c_elements[1] - elements_j[1])**2 + (last_c_elements[2] - elements_j[2])**2)
        current_boxes = [last_circ, jl]
        last_distances[dist] = (current_boxes)

print("the last distance is: ", last_distances)
min_last = min(last_distances)
print("min last is: ", last_distances[min_last])

circ_counter = 0
for idx, thing in enumerate(all_circuits):
    all_circuits[idx] = set(thing)

#two_x = ['14041,98765,696', '19525,88390,6197']

two_x = last_distances[min_last]
final = 1

for x in two_x:
    coords = x.split(",")
    final *= int(coords[0])

print(final)
#result is = 274150525