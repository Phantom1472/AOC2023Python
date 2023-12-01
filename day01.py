import re

from aocd import get_data


def part1(lines):
    total = 0
    for line in lines:
        all_digits = re.findall('\d', line)
        total += int(f'{all_digits[0]}{all_digits[-1]}')
    return total


def part2(lines):
    word_to_digit = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
                     'eight': '8', 'nine': '9'}
    words_regex = '(?=(' + '|'.join(word_to_digit.keys() | word_to_digit.values()) + '))'
    total = 0
    for line in lines:
        words_and_digits = re.findall(words_regex, line)
        # words_and_digits = [word_to_digit.get(word_or_digit, word_or_digit) for word_or_digit in words_and_digits]
        total += int(f'{words_and_digits[0]}{words_and_digits[-1]}')
    return total


def main():
    lines = get_data(day=1, year=2023).splitlines()
    print('day 1')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
