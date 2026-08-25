def part_1(entry):
    game_id, rounds = entry.split(':')
    rounds = rounds.strip().split(';')

    for game_round in rounds:
        cubes = game_round.split(',')
        for cube in cubes:
            cube = cube.strip().split(' ')
            cube_qtd = int(cube[0])
            match cube[1]:
                case 'red':
                    if cube_qtd > 12:
                        return 0
                case 'green':
                    if cube_qtd > 13:
                        return 0
                case 'blue':
                    if cube_qtd > 14:
                        return 0

    return int(game_id.strip().split()[1])

def part_2(entry):
    game_id, rounds = entry.split(':')
    rounds = rounds.strip().split(';')
    
    red = 0
    green = 0
    blue = 0

    for game_round in rounds:
        cubes = game_round.split(',')
        for cube in cubes:
            cube = cube.strip().split(' ')
            cube_qtd = int(cube[0])
            match cube[1]:
                case 'red':
                    if cube_qtd > red:
                        red = cube_qtd
                case 'green':
                    if cube_qtd > green:
                        green = cube_qtd
                case 'blue':
                    if cube_qtd > blue:
                        blue = cube_qtd

    return red * green * blue

gameid_sum = 0
gamecubes_sum = 0
while True:
    try:
        entry = input()
        gameid_sum += part_1(entry)
        gamecubes_sum += part_2(entry)
    except EOFError:
        break

print(gameid_sum)
print(gamecubes_sum)
