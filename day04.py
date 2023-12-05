from collections import Counter

from aocd import get_data


def part1(lines):
    total = 0
    for line in lines:
        card = list(map(str.split, line.split(':')[1].split('|')))
        card = [set(map(int, x)) for x in card]
        winning_numbers = len(card[0] & card[1])
        if winning_numbers:
            total += 2 ** (winning_numbers - 1)
    return total


def part2(lines):
    card_copies = Counter(range(1, len(lines) + 1))
    for index, line in enumerate(lines, 1):
        card = list(map(str.split, line.split(':')[1].split('|')))
        card = [set(map(int, x)) for x in card]
        for num in range(index + 1, index + 1 + len(card[0] & card[1])):
            card_copies[num] += card_copies[index]
    return card_copies.total()


def main():
    lines = get_data(day=4, year=2023).splitlines()
    print('day 4')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
