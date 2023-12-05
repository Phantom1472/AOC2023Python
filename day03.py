import math
from itertools import product, chain

from aocd import get_data


def part1(lines):
    mask = []
    for line in lines:
        mask_line = []
        for char in line:
            if char.isdigit() or char == '.':
                mask_line.append(0)
            else:
                mask_line.append(1)
        mask.append(mask_line)
    expand_mask(mask, lines)
    new_lines = []
    for x in range(len(mask)):
        new_line = []
        for y in range(len(mask[0])):
            if mask[x][y] == 2:
                new_line.append(lines[x][y])
            else:
                new_line.append(' ')
        new_lines.append(''.join(new_line).split())
    new_lines = [list(map(int, line)) for line in new_lines]
    return sum(map(sum, new_lines))


def expand_mask(mask, lines):
    offsets = list(product([-1, 0, 1], [-1, 0, 1]))
    offsets.remove((0, 0))
    for x in range(len(mask)):
        for y in range(len(mask[0])):
            if mask[x][y] == 1:
                expand_mask_aux(mask, lines, offsets, x, y)


def expand_mask_aux(mask, lines, offsets, x, y, gear_id=2):
    abs_inxs = [(x + x_offset, y + y_offset) for (x_offset, y_offset) in offsets]
    abs_inxs = [(new_x, new_y) for (new_x, new_y) in abs_inxs if
                (0 <= new_x < len(mask)) and (0 <= new_y < len(mask[0]))]
    for new_x, new_y in abs_inxs:
        if mask[new_x][new_y] == 0 and lines[new_x][new_y].isdigit():
            mask[new_x][new_y] = gear_id
            expand_mask_aux(mask, lines, offsets, new_x, new_y, gear_id)


def part2(lines):
    mask = []
    for line in lines:
        mask_line = []
        for char in line:
            if char == '*':
                mask_line.append(1)
            else:
                mask_line.append(0)
        mask.append(mask_line)
    max_gear_id = expand_mask2(mask, lines)
    total = 0
    for gear_id in range(2, max_gear_id):
        new_lines = []
        for x in range(len(mask)):
            new_line = []
            for y in range(len(mask[0])):
                if mask[x][y] == gear_id:
                    new_line.append(lines[x][y])
                else:
                    new_line.append(' ')
            new_lines.append(''.join(new_line).split())
        new_lines = [list(map(int, line)) for line in new_lines]
        flattened = list(chain.from_iterable(new_lines))
        if len(flattened) == 2:
            total += math.prod(flattened)
    return total


def expand_mask2(mask, lines):
    offsets = list(product([-1, 0, 1], [-1, 0, 1]))
    offsets.remove((0, 0))
    gear_id = 2
    for x in range(len(mask)):
        for y in range(len(mask[0])):
            if mask[x][y] == 1:
                expand_mask_aux(mask, lines, offsets, x, y, gear_id)
                gear_id += 1
    return gear_id


def main():
    lines = get_data(day=3, year=2023).splitlines()
    print('day 3')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
