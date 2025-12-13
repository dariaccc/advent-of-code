
with open("Day 6/input2.txt", "r") as file:
    input = [line.strip() for line in file]

print(input)
print(len(input))

length = len(input)

input_list = []

for idx_l, list in enumerate(input[0:length:1]):
    j = list.split(" ")
    for _ in range(5):
        for idx_list, current_number in enumerate(j):
            if current_number == "" or current_number == " ":
                j.pop(idx_list)
    
    if idx_l == length - 1:
        operators = j
    else:
        input_list.append(j)

print(input_list)
print(operators)

n = 0
total = []
for _ in range(len(input_list[0])):
    sum = 0
    for i in input_list:
        if operators[n] == "*":
            if sum == 0:
                sum = 1
            sum *= int(i[n])
        if operators[n] == "+":
            sum += int(i[n])
    total.append(sum)
    n += 1

print(total)
num = 0
for idx in range(len(total)):
    print(num)
    num += total[idx]
print(num)