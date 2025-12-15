
#ready
with open("Day 7/input2.txt", "r") as file:
    input = [line.strip() for line in file]

paths = 0
char_list = []
len_list = int(len(input) / 2 - 1)
r_list = []

for _ in range(2):
    previous = input[0]
    new_input = [previous]
    old_char_list = char_list
    char_list = []
    rs = 0
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
                    idx_c = int(idx_i/2)
                    for idx_r, c in enumerate(old_char_list):
                        if c == "R":
                            r_list.append(idx_r)

                    if not r_list:
                        if int(idx_i/2) == len(old_char_list):
                            char_list.append("R")
                        else:
                            char_list.append("L")
                    
                    #if idx_c


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


#print(paths)
