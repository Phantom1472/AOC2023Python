import math
import re
from itertools import cycle

from aocd import get_data


def part1(lines):
    instructions = lines[0]
    raw_network = lines[2:]
    network = {}
    for node in raw_network:
        start, left, right = re.split(r'\W+', node)[:-1]
        network[start] = {'L': left, 'R': right}
    current = 'AAA'
    steps = 0
    for instruction in cycle(instructions):
        next_node = network[current][instruction]
        steps += 1
        if next_node == 'ZZZ':
            break
        current = next_node
    return steps


def part2(lines):
    instructions = lines[0]
    raw_network = lines[2:]
    network = {}
    for node in raw_network:
        start, left, right = re.split(r'\W+', node)[:-1]
        network[start] = {'L': left, 'R': right}
    currents = [node for node in network if node[-1] == 'A']
    lengths = []
    for current in currents:
        steps = 0
        for instruction in cycle(instructions):
            next_node = network[current][instruction]
            steps += 1
            if next_node[-1] == 'Z':
                lengths.append(steps)
                break
            current = next_node
    return math.lcm(*lengths)


def main():
    lines = get_data(day=8, year=2023).splitlines()
    print('day 8')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
