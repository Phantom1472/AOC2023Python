from aocd import get_data


def part1(lines):
    return aux(lines)


def part2(lines):
    return aux(lines, -1)


def aux(lines, direction=1):
    lines = [[int(x) for x in line.split()][::direction] for line in lines]
    total = 0
    for line in lines:
        new_lines = [line]
        while True:
            if len(set(new_lines[-1])) == 1:
                break
            else:
                last_line = new_lines[-1]
                z = zip(last_line, last_line[1:])
                new_last_line = [y - x for x, y in z]
                new_lines.append(new_last_line)
        total += sum([line[-1] for line in new_lines])
    return total


def main():
    lines = get_data(day=9, year=2023).splitlines()
    print('day 9')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
