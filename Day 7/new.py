
# #ready
# with open("Day 7/input2.txt", "r") as file:
#     input = [line.strip() for line in file]

# first_input = input
# paths = 0
# char_list = []
# len_list = int(len(input) / 2 - 1)
# r_list = []
# finished = False

# #while not finished:
# for _ in range(10):
#     previous = input[0]
#     new_input = [previous]
#     old_char_list = char_list
#     char_list = []
#     rs = 0
#     r_list = []

#     for idx_r, c in enumerate(old_char_list):
#         if c == "R":
#             r_list.append(idx_r)

#     for idx_i, i in enumerate(input[1::]):
        
#         i = list(i)
#         for idx, char in enumerate(previous):
#             if char == "S":
#                 i[idx] = "|"
#             elif char == "^" and pre_previous[idx] != ".":

#                 if idx_i == 0:
#                     i[idx - 1] = "|"
#                     char_list.append("L")
#                 else:
#                     idx_c = int(idx_i/2) - 1
#                     print(idx_c + 1, r_list)
#                     if not r_list:
#                         if idx_c == len(old_char_list) - 1:
#                             char_list.append("R")
#                             i[idx + 1] = "|"
#                         else:
#                             i[idx - 1] = "|"
#                             char_list.append("L")
#                     elif idx_c + 1 == r_list[0] and all(rs == "R" for rs in old_char_list[idx_c + 2::]):
#                         print("here1")
#                         char_list.append("R")
#                         i[idx + 1] = "|"
#                     elif idx_c == r_list[0]:# and char_list[-1] != "R":
#                         if char_list[-1] != "R":
#                             print("here2")
#                             char_list.append("R")
#                             i[idx + 1] = "|"
#                         else:
#                             print("here other 2")
#                             char_list.append("L")
#                             i[idx - 1] = "|"
#                     elif len(char_list) >= len(old_char_list):
#                         i[idx - 1] = "|"
#                         char_list.append("L")
#                     elif len(char_list) <= len(old_char_list) and idx_c in r_list:
#                         print("here for test")
#                         i[idx + 1] = "|"
#                         char_list.append("R")
#                     elif char_list != [] and char_list[-1] == "R" and old_char_list[idx_c] == "L":
#                         #issue is here when current is L AND next is L, it should be R
#                         #print(len(old_char_list), idx_c)
#                         if idx_c != len(old_char_list) - 1 and all(ls == "L" for ls in old_char_list[idx_c + 2::]):
#                             print("here3 other test")
#                             char_list.append("L")
#                             i[idx - 1] = "|"
#                         else:
#                             print("here3")
#                             char_list.append("R")
#                             i[idx + 1] = "|"
#                         #print(char_list)
#                     else:
#                         print("here4")
#                         i[idx - 1] = "|"
#                         char_list.append("L")

#             elif char == "|" and i[idx] != "^":
#                 i[idx] = "|"

#         i = "".join(i)
#         new_input.append(i)
#         pre_previous = previous
#         previous = i


#     for j in new_input:
#         print(j)

#     print(char_list)
#     paths += 1
#     input = first_input

#     if char_list == ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']: finished = True

# print(paths)

# #DFS algorithm


test_list =  ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'R', 'L', 'R']
print(test_list)
idx_c = 8
print(idx_c)
if idx_c != len(test_list) and all(rs == "R" for rs in test_list[idx_c + 1::]):
    print("ALL R")