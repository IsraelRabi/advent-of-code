def how_many_winning_numbers(card):
    result = 0
    card = card.split(':')[1].split('|')

    winning_numbers = card[0].strip().split()
    for choosen_number in card[1].strip().split():
        if choosen_number in winning_numbers:
            result += 1

    return result


def part_1(cards):
    cards = [x.split(':')[1].split('|') for x in cards]
    points = []

    for card in cards:
        result = 0
        winning_numbers = card[0].strip().split()
        for choosen_number in card[1].strip().split():
            if choosen_number in winning_numbers:
                if result == 0:
                    result += 1
                else:
                    result *= 2
        points.append(result)

    return sum(points) 


def part_2(cards):
    cards_total = [1 for i in range(len(cards))]

    for i in range(len(cards)):
        winning_n = how_many_winning_numbers(cards[i])
        if winning_n > 0:
            total_cards_i = cards_total[i]
            boundary = i + 1
            for j in range(winning_n):
                cards_total[boundary] += total_cards_i
                boundary += 1

    return sum(cards_total)



cards = []
while True:
    try:
        cards.append(input())
    except EOFError:
        break

#print(part_1(cards))
print(part_2(cards))
