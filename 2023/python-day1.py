def name_to_number(line, i):
    match line[i]:
        case 'o':
            possibilite = line[i:i+3]
            if possibilite == 'one':
                return 1
        case 'e':
            possibilite = line[i:i+5]
            if possibilite == 'eight':
                return 8
        case 'n':
            possibilite = line[i:i+4]
            if possibilite == 'nine':
                return 9
        case 't':
            possibilite = line[i:i+3]
            if possibilite == 'two':
                return 2
            else:
                possibilite = line[i:i+5]
                if possibilite == 'three':
                    return 3
        case 'f':
            possibilite = line[i:i+4]
            if possibilite == 'four':
                return 4
            elif possibilite == 'five':
                return 5
        case 's':
            possibilite = line[i:i+3]
            if possibilite == 'six':
                return 6
            else:
                possibilite = line[i:i+5]
                if possibilite == 'seven':
                    return 7
    return 0

def calibration_values(line):
    possibilities = ['o', 't', 'f', 's', 'e', 'n']
    numbers = []
    for i in range(len(line)):
        char = line[i]
        if char.isdigit():
            numbers.append(char)
        elif char in possibilities:
            possible_num = name_to_number(line, i)
            if possible_num != 0:
                numbers.append(str(possible_num))
    if len(numbers) == 1:
        return int(numbers[0] * 2)
    return int(numbers[0] + numbers[-1])

sum_of_numbers = 0
while True:
    try:
        entry = input()
        sum_of_numbers += calibration_values(entry)
    except EOFError:
        break
print(sum_of_numbers)
