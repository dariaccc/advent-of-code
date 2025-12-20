#ready

with open("Day 7/input.txt", "r") as file:
    tree = [line.strip() for line in file]

for idx_tree, _ in enumerate(tree[1::2]):
    tree.remove(tree[idx_tree + 1])

print(tree)

n = 0
dic = dict()

for _ in tree[0]:
    dict_key = n
    dic[n] = 0
    n += 1

for row in tree:
    row = list(row)

    for idx, i in enumerate(row):
        if i == "S":
            dic[idx] = 1
        elif i == "^":
            dic[idx + 1] += dic[idx]
            dic[idx - 1] += dic[idx]
            dic[idx] = 0

print("final dict: ", dic)

total = 0
for value in dic.values():
    total += value

print(total)