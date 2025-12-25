
#ready
with open("Day 6/input.txt", "r") as file:
    input = [line for line in file]

print(input)

length = len(input)
operators = list(input[length - 1])
print(operators)

while " " in operators:
    operators.remove(" ")

print(operators)
input.pop(length - 1)

input_list = []

equations = len(operators)
print(equations)

e = []

zipped_list = zip(*input)
start = 0
stop = 2

for z in zipped_list:
        its = ""
        print(z)
        for char in z:
            print(char)
            its += char
            its = its.strip()

        print("its: ", its)
        e.append(its)

number, prev_num = 0, 0
result = 1
results = []

for element in e:
    print("index is: ", number)

    if number > prev_num:
        print("here")
        if operators[number] == "*":
            result = 1
        else:
            result = 0
    prev_num = number 
    
    if element != " " and element != "":
        print(element)
        if operators[number] == "*":
            result *= int(element)
        elif operators[number] == "+":
            result += int(element)
    else:
        number += 1
        print("result is: ", result)
        results.append(result)

print(results)

total = 0
for result in results:
    total += result

print(total)