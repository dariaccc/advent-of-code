import math

with open("Day 8/input.txt", "r") as file:
    input = [line.strip() for line in file]

#print(input)
all_distances= []
start = 0

for idx_i, i in enumerate(input[:len(input)-1:]):
    min_dist = 10000
    distances = []
    elements = []
    for element in i.split(","):
        elements.append(int(element))
    
    for idx_j, j in enumerate(input[start::]):
        if i != j:
            elements_j = []
            for element_j in j.split(","):
                elements_j.append(int(element_j))

            dist = math.sqrt((elements[0] - elements_j[0])**2 + (elements[1] - elements_j[1])**2 + (elements[2] - elements_j[2])**2)

            distances.append(dist)
    start += 1
    all_distances.append(distances)

#print(all_distances)
circuit = 0
all_circuits = [[]]

for x in range(1000):
    minimums = []
    temp = []
    minimum_i_idx, minimum_j_idx = [], []
    for idx_d,d in enumerate(all_distances):
        min_d_idx = d.index(min(d))
        minimums.append(min(d))
        minimum_j_idx.append(min_d_idx)

    minimum_i_idx = minimums.index(min(minimums))
 
    add_on = minimum_i_idx + 1
    #print(input[minimum_i_idx], input[minimum_j_idx[minimum_i_idx] + add_on])

    broken_loop = False
    in_c = False
    if x == 0:
        all_circuits[0].append(input[minimum_i_idx])
        all_circuits[0].append(input[minimum_j_idx[minimum_i_idx] + add_on])
    else:
        for idx_c, circuit in enumerate(all_circuits):

            if (str(input[minimum_i_idx]) in circuit) and (str(input[minimum_j_idx[minimum_i_idx] + add_on]) in circuit):
 
                in_c = True
                break
            elif str(input[minimum_i_idx]) in circuit:
                for circuit2 in all_circuits:
                    if str(input[minimum_j_idx[minimum_i_idx] + add_on]) in circuit2 and circuit != circuit2:
                        #print("HERE: ", circuit, circuit2)
                        all_circuits.pop(idx_c)

                        to_pop = all_circuits.index(circuit2)
                        all_circuits.pop(to_pop)
                        #print(all_circuits)
                        all_circuits.append(circuit + circuit2)
                        broken_loop = True
                        break

                if not broken_loop:
                    all_circuits[idx_c].append(input[minimum_j_idx[minimum_i_idx] + add_on])
                in_c = True
                break
            elif str(input[minimum_j_idx[minimum_i_idx] + add_on]) in circuit:
                #  print("one in 1")
                all_circuits[idx_c].append(input[minimum_i_idx])
                in_c = True
                break

        if not in_c:
            temp.append(input[minimum_i_idx])
            temp.append(input[minimum_j_idx[minimum_i_idx] + add_on])

            all_circuits.append(temp)

    #print('all circuits: ', all_circuits)
    all_distances[minimum_i_idx][minimum_j_idx[minimum_i_idx]] = 100000000

print('all circuits: ', all_circuits)

circuit_lengths = []
for c in all_circuits:
    circuit_lengths.append(len(c))

print(circuit_lengths)
prev_value = 1

for _ in range(3):
    value = max(circuit_lengths)
    print(max(circuit_lengths))
    circuit_lengths.pop(circuit_lengths.index(max(circuit_lengths)))
    value *= prev_value
    prev_value =- value

print(value)