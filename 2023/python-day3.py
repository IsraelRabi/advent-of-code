def part_1(parts):

    count = 0
    for r, row in enumerate(parts):
        digits = []
        digit = ''
        count = firts_index = last_index = 0
        while count < len(row):
            if row[count].isdigit():
                    firts_index = count
                if count < len(row) and row[count + 1].isdigit():
                    last_index = count




            count += 1

    return 0


parts = []
while True:
    try:
        entry = input()
        parts.append(entry)
    except EOFError:
        break
#print(part_1(parts))
part_1(parts)
