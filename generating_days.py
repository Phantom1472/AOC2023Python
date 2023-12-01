for i in range(1, 26):
    with open(f'day{i:02}.py', 'w') as FILE:
        FILE.write(f'''from aocd import get_data


def part1(lines):
    return lines


def part2(lines):
    return lines


def main():
    lines = get_data(day={i}, year=2023).splitlines()
    print('day {i}')
    print(f'part1: {{part1(lines)}}')
    print(f'part2: {{part2(lines)}}')


if __name__ == '__main__':
    main()
''')
