with open("Day 3/input.txt", "r") as file:
    bank = [line.strip() for line in file]

print(bank)
joltage = []

for i in bank:
    volt12 = []
    search_list = []
    stop = len(i) - 12

    i = list(i)

    index = 0
    x = 1
    for n in range(12)[::-1]:
        
        j = i[index:stop + 1:1]
        print(j)
        max_value = max(j)
        
        print(max_value)
        index = index + (j.index(max(j))) + 1
        print("index: ", index)

        stop = len(i) - n
        x += 1
        volt12.append(max_value)
    joltage.append(volt12)

print(joltage)

sums = 0
for bank in joltage:
    banks = ""
    for a in bank:
        banks += a
    print(banks)
    banks = int(banks)
    sums += banks

print(sums)