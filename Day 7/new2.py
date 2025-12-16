
#ready
with open("Day 7/input.txt", "r") as file:
    input = [line.strip() for line in file]

first_input = input
paths = 0
char_list = []
r_list = []
finished = False

while not finished:
#for n in range(10):
    previous = input[0]
    new_input = [previous]
    old_char_list = char_list
    char_list = []
    r_list = []
    switch = False
    last_idx = len(old_char_list)-1

    for idx_r, c in enumerate(old_char_list):
        if c == "R":
            r_list.append(idx_r)

    for idx_i, i in enumerate(input[1::]):
        
        i = list(i)
        for idx, char in enumerate(previous):
            if char == "S":
                i[idx] = "|"
            elif char == "^" and pre_previous[idx] != ".":
                if paths == 0:
                    i[idx - 1] = "|"
                    char_list.append("L")
                else:
                    idx_c = int(idx_i/2) - 1
                    ocl_index = len(old_char_list) - 1

                    #print(idx_c)
                    if idx_c != len(old_char_list) and all(rs == "R" for rs in old_char_list[idx_c + 1::]) and not switch: # om allt till höger om index är R
                        print(last_idx, idx_c) #| PROBLEM UP HERE
                        print("here1")
                        #it enters HERE for some reason
                        char_list.append("R")
                        i[idx + 1] = "|"
                        switch = True
                    elif idx_c == ocl_index and not switch: #om det är sista bokstaven
                        print("here2")
                        char_list.append("R")
                        i[idx + 1] = "|"
                    elif switch:
                        print("switch")
                        i[idx - 1] = "|"
                        char_list.append("L")
                    elif idx_c < len(old_char_list) and old_char_list[idx_c] == "R" and not switch: #change to this: old_char_list[idx_c] == "R" and not switch
                        #print("here3")
                        char_list.append("R")
                        i[idx + 1] = "|"
                    else:
                        #print("here4")
                        i[idx - 1] = "|"
                        char_list.append("L")

            elif char == "|" and i[idx] != "^":
                i[idx] = "|"

        i = "".join(i)
        new_input.append(i)
        pre_previous = previous
        previous = i


    # for j in new_input:
    #     print(j)

    print(char_list)
    paths += 1
    input = first_input
    if char_list == old_char_list: 
        print("ERROR")
        break

    if all(rs == "R" for rs in char_list): 
        print("FINISH")
        finished = True

print(paths)

#DFS algorithm