import math

from aocd import get_data


def part1(lines):
    times, distances = [list(map(int, line.split(':')[1].split())) for line in lines]
    ways_list = []
    for time, distance in zip(times, distances):
        ways_list.append(
            len(list(filter(lambda x: x > distance, map(math.prod, zip(range(0, time), range(time, 0, -1)))))))
    return math.prod(ways_list)


def part2(lines):
    time, distance = [int(line.replace(' ', '').split(':')[1]) for line in lines]
    return len(list(filter(lambda x: x > distance, map(math.prod, zip(range(0, time), range(time, 0, -1))))))


def main():
    lines = get_data(day=6, year=2023).splitlines()
    print('day 6')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
