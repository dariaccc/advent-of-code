
#ready
with open("Day 7/input2.txt", "r") as file:
    input = [line.strip() for line in file]

paths = 0
char_list = []
len_list = int(len(input) / 2 - 1)
r_list = []

for _ in range(3):
    previous = input[0]
    new_input = [previous]
    old_char_list = char_list
    char_list = []
    rs = 0

    for idx_r, c in enumerate(old_char_list):
        if c == "R":
            r_list.append(idx_r)

    for idx_i, i in enumerate(input[1::]):
        
        i = list(i)
        for idx, char in enumerate(previous):
            if char == "S":
                i[idx] = "|"
            elif char == "^" and pre_previous[idx] != ".":

                if len(old_char_list) < len_list:
                    i[idx - 1] = "|"
                    char_list.append("L")
                else:
                    idx_c = int(idx_i/2) - 1

                    if not r_list:
                        if idx_c == len(old_char_list) - 1:
                            char_list.append("R")
                            i[idx + 1] = "|"
                        else:
                            char_list.append("L")
                            i[idx - 1] = "|"
                    elif all(rs == "R" for rs in old_char_list[idx_c::]):
                        print(idx_c)
                        print(all(rs == "R" for rs in old_char_list[idx_c::]))
                        i[idx + 1] = "|"
                        char_list.append("R")
                    else:
                        i[idx - 1] = "|"
                        char_list.append("L")


            elif char == "|" and i[idx] != "^":
                i[idx] = "|"

        i = "".join(i)
        new_input.append(i)
        pre_previous = previous
        previous = i
    paths += 1
    input = new_input

for j in new_input:
    print(j)

print(char_list)

#DFS algorithm

#next iteration (range3) - should be ['L', 'L', 'L', 'L', 'L', 'R', 'L']
#problem now is - we are on the LAST element when we check the last element
