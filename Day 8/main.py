import math

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

#print(distances)
print(len(distances))

#circuit = 0
all_circuits = []

for _ in range(1000):
    min_dist = min(distances)
    boxes = distances[min_dist]
    print(min_dist)
    print(boxes)
    distances.pop(min_dist)

    all_circuits.append(boxes)

print(all_circuits)
print(len(all_circuits))

start = 1
stop_loop = 0
while stop_loop < len(all_circuits) - 1:
    broken = False
    circuit = all_circuits[stop_loop]
    print("circ is: ", circuit)

    for sec_circuit in all_circuits[start::]:
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


circ_counter = 0
for idx, thing in enumerate(all_circuits):
    all_circuits[idx] = set(thing)


print("\n", all_circuits)
print(circ_counter)


circuit_lengths = []
for c in all_circuits:
    circuit_lengths.append(len(c))

print(circuit_lengths)
prev_value = 1

for _ in range(3):
    value = max(circuit_lengths)
    circuit_lengths.pop(circuit_lengths.index(max(circuit_lengths)))
    value *= prev_value
    prev_value =- value

print(value)