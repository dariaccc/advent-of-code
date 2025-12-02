
with open('input.txt', 'r') as file:
    input = [line.strip() for line in file]

def r_iterate(variable, number):
    passed_zeros = int(number/100)
    temp = number % 100
    temp_variable = variable + temp
    if (temp_variable > 99):
        variable = temp_variable - 100
        if(variable != 0):
            passed_zeros += 1
    else:
        variable += temp
    return(variable, passed_zeros)

def l_iterate(variable, number):
    passed_zeros = int(number/100)
    temp = number % 100 
    temp_variable = variable - temp
    if (temp_variable < 0):
        if(variable != 0):
            passed_zeros += 1
        variable = 100 + temp_variable
    else:
        variable -= temp
    return(variable, passed_zeros)

variable = 50
password = 0
extra_zeros = 0

for i in input:
    extra_zeros = 0
    direction = i[0]

    l = list(i)
    l[0] = direction
    number = ""
    for num in l[1:]:
        number += num

    number = int(number)

    if(direction == "R"):
        if(number > (99 - variable)):
            variable, extra_zeros = r_iterate(variable, number)
        else:
            variable += number
    elif(direction == "L"):
        if(variable < number):
            variable, extra_zeros = l_iterate(variable, number)
        else:
            variable -= number
    
    if(variable == 0):
        password += 1

    password += extra_zeros

print("password: ", password)