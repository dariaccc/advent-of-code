
with open("Day 6/input2.txt", "r") as file:
    input = [line.strip() for line in file]

print(input)
print(len(input))

length = len(input)

operators = []
input_list = []

for idx_l, list in enumerate(input[0:length:1]):
    j = list.split(" ")
    for idx_list, current_number in enumerate(j):
        print(current_number)
        if current_number == "" or current_number == " ":
            j.pop(idx_list)
    
    if idx_l == length - 1:
        for idx_e, empty in enumerate(j):
            if empty == "" or empty == " ":
                j.pop(idx_e)
        operators.append(j)
    else:
        input_list.append(j)

print(input_list)
print(operators)

rowsum, row2sum, row3sum, row4sum = 0, 0, 0, 0
rowsumtotal = []

# for i in input[0:length - 1:1]:
#     j = i.split(" ")
#     for idx_e, empty in enumerate(j):
#         if empty == "":
#             j.pop(idx_e)

#     for idx_k, k in enumerate(j):
#         #print(j)
#         n = 0
        
#         if idx_k % 4 == n:
#             if operators[n] == "+":
#                 rowsum += int(k)
#             elif operators[0] == "*":
#                 if rowsum == 0:
#                     rowsum = 1
#                 rowsum *= int(k)
#         n += 1
#         rowsumtotal.append(rowsum)
        # elif idx_k % 4 == 1:
        #     row2.append(k)
        # elif idx_k % 4 == 2:
        #     row3.append(k)
        # elif idx_k % 4 == 3:
        #     row4.append(k)

# print(rowsum)
# print(rowsumtotal)