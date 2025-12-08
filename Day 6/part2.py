
with open("Day 6/input2.txt", "r") as file:
    input = [line.strip() for line in file]

# print(input)
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
        for idx_n,number in enumerate(j):
            j[idx_n] = int(number)
        input_list.append(j)

print(input_list)
print(operators)

n = 0
total = []
temp = []
start = 0
stop = len(input_list) - 1
for _ in range(len(input_list[0])):
    sum = 0
    # max_length = max(input_list[n])
    # print(max_length)

    for i in input_list:
        #print("i: ", i[n])
        # if operators[n] == "*":
        #     if sum == 0:
        #         sum = 1
        for _ in range(start, stop):
            temp.append(i)
        total.append(temp)
        start = stop
        stop += len(input_list)
        # if operators[n] == "+":
    #total.append(sum)
    n += 1

print(total)
num = 0

start = 0
stop = len(input_list) - 1
temp = []

# for _ in range(length):
#     for k in total[start:stop:1]:
#         temp.append(k)
#     total.append
#     start = stop
#     stop += len(input_list)

# print(total)

# for idx in range(len(total)):
#     #print(total[idx])
#     num += total[idx]
# #print(num)