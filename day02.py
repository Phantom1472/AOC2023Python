import math
import re

from aocd import get_data


def part1(games):
    total = 0
    for raw_game in games:
        draws, game_id = get_draws_game_id(raw_game)
        if is_game_valid(draws):
            total += game_id
    return total


def part2(games):
    total = 0
    for raw_game in games:
        draws, game_id = get_draws_game_id(raw_game)
        total += get_power_set(draws)
    return total


def get_draws_game_id(raw_game):
    game = re.split('[:;]', raw_game)
    game_id = int(game[0].split()[1])
    draws = list(map(str.strip, game[1:]))
    draws = [re.split(', ', game) for game in draws]
    draws = [[(int(sub_draw.split()[0]), sub_draw.split()[1]) for sub_draw in draw] for draw in draws]
    return draws, game_id


def is_game_valid(draws):
    inventory = {'red': 12, 'green': 13, 'blue': 14}
    for draw in draws:
        for sub_draw in draw:
            if sub_draw[0] > inventory[sub_draw[1]]:
                return False
    return True


def get_power_set(draws):
    minimums = {'red': 0, 'green': 0, 'blue': 0}
    for draw in draws:
        for sub_draw in draw:
            minimums[sub_draw[1]] = max(minimums[sub_draw[1]], sub_draw[0])
    return math.prod(minimums.values())


def main():
    lines = get_data(day=2, year=2023).splitlines()
    print('day 2')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
