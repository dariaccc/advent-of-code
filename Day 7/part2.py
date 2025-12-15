
import random
from tqdm import tqdm

with open("Day 7/input2.txt", "r") as file:
    input = [line.strip() for line in file]

previous = input[0]
new_input = [previous]
print(input)

counter = 0
paths = 0
total_paths = []

#while new_input not in total_paths:
for i in tqdm(range(3000)):
    previous = input[0]
    new_input = [previous]
    for i in input[1::]:
        i = list(i)
        for idx, char in enumerate(previous):
            if char == "S":
                i[idx] = "|"
            elif char == "^" and pre_previous[idx] != ".":
                random_int = random.randint(1,2)
                if random_int == 1:
                    i[idx + 1] = "|"
                elif random_int == 2:
                    i[idx - 1] = "|"
            elif char == "|" and i[idx] != "^":
                i[idx] = "|"
        i = "".join(i)
        new_input.append(i)
        pre_previous = previous
        previous = i
    if new_input not in total_paths:
        total_paths.append(new_input)
        paths += 1


# for t_path in total_paths:
#     for t in t_path:
#         print(t)

# print("number of paths:", paths)