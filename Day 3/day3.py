with open("Day 3/input.txt", "r") as file:
    bank = [line.strip() for line in file]

print(bank)
joltage = 0

for i in bank:
    max_left = 0
    max_right = 0
    index = 0
    for j in i[:-1]:
        j = int(j)
        if j > max_left:
            max_left = j
    
    for k in i[i.index(str(max_left))+1::1]:
        k = int(k)
        if k > max_right:
            max_right = k
    
    str_max = str(max_left) + str(max_right)
    print(str_max)
    joltage += int(str_max)

print(joltage)