
with open("Day 7/input2.txt", "r") as file:
    input = [line.strip() for line in file]

previous = input[0]
new_input = [previous]
counter = 0

for i in input[1::]:
    i = list(i)
    for idx, char in enumerate(previous):
        if char == "S":
            i[idx] = "|"
        elif char == "^" and pre_previous[idx] != ".":
            i[idx + 1] = "|"
            i[idx - 1] = "|"
            counter += 1
        elif char == "|" and i[idx] != "^":
            i[idx] = "|"
    i = "".join(i)
    new_input.append(i)
    pre_previous = previous
    previous = i

for j in new_input:
    print(j)

print(counter)