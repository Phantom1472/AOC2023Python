from collections import Counter
from enum import IntEnum, auto

from aocd import get_data


class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE = auto()
    FULL_HOUSE = auto()
    FOUR = auto()
    FIVE = auto()


def part1(lines):
    card_order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    hand_bid_list = [x.split() for x in lines]
    hand_bid_list = [(x[0], int(x[1])) for x in hand_bid_list]
    hand_type_list = []
    for (hand, bid) in hand_bid_list:
        hand_type = get_hand_type(hand)
        hand_ints = [card_order.index(char) for char in hand]
        hand_type_list.append((hand_type, hand_ints, bid))
    hand_type_list.sort()
    total = 0
    for index, (hand_type, hand_ints, bid) in enumerate(hand_type_list, 1):
        total += bid * index
    return total


def get_hand_type(hand):
    hand_counter = Counter(hand)
    most_common = hand_counter.most_common()
    if most_common[0][1] == 5:
        return HandType.FIVE
    elif most_common[0][1] == 4:
        return HandType.FOUR
    elif most_common[0][1] == 3 and most_common[1][1] == 2:
        return HandType.FULL_HOUSE
    elif most_common[0][1] == 3:
        return HandType.THREE
    elif most_common[0][1] == 2 and most_common[1][1] == 2:
        return HandType.TWO_PAIR
    elif most_common[0][1] == 2:
        return HandType.ONE_PAIR
    else:
        return HandType.HIGH_CARD


def part2(lines):
    card_order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    hand_bid_list = [x.split() for x in lines]
    hand_bid_list = [(x[0], int(x[1])) for x in hand_bid_list]
    hand_type_list = []
    for (hand, bid) in hand_bid_list:
        if 'J' not in hand:
            hand_type = get_hand_type(hand)
        else:
            hand_type = get_hand_type2(hand)
        hand_ints = [card_order.index(char) for char in hand]
        hand_type_list.append((hand_type, hand_ints, bid))
    hand_type_list.sort()
    total = 0
    for index, (hand_type, hand_ints, bid) in enumerate(hand_type_list, 1):
        total += bid * index
    return total


def get_hand_type2(hand):
    j_count = hand.count('J')
    hand_counter = Counter(hand.replace('J', ''))
    most_common = hand_counter.most_common()
    if not most_common:
        return HandType.FIVE
    elif most_common[0][1] == 4:
        return HandType.FIVE
    elif most_common[0][1] == 3:
        if j_count == 1:
            return HandType.FOUR
        else:
            return HandType.FIVE
    elif len(most_common) >= 2 and most_common[0][1] == 2 and most_common[1][1] == 2:
        return HandType.FULL_HOUSE
    elif most_common[0][1] == 2:
        if j_count == 1:
            return HandType.THREE
        elif j_count == 2:
            return HandType.FOUR
        else:
            return HandType.FIVE
    else:
        if j_count == 1:
            return HandType.ONE_PAIR
        elif j_count == 2:
            return HandType.THREE
        elif j_count == 3:
            return HandType.FOUR
        else:
            return HandType.FIVE


def main():
    lines = get_data(day=7, year=2023).splitlines()
    print('day 7')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
