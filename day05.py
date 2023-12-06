from itertools import batched

from aocd import get_data


def part1(almanac):
    seeds, *mappings = almanac
    seeds = list(map(int, seeds.split()[1:]))
    mappings = [[[int(y) for y in x.split()] for x in mapping.split('\n')[1:]] for mapping in mappings]
    location_numbers = []
    for seed in seeds:
        for mapping in mappings:
            seed = get_dest_value(seed, mapping)
        location_numbers.append(seed)
    return min(location_numbers)


def get_dest_value(src, mapping):
    for dest_start, src_start, length in mapping:
        if src_start <= src < src_start + length:
            return src + (dest_start - src_start)
    return src


def part2(almanac):
    seeds, *mappings = almanac
    seeds = list(map(int, seeds.split()[1:]))
    seeds = [[x, x + y - 1] for x, y in batched(seeds, 2)]
    mappings = [[[int(y) for y in x.split()] for x in mapping.split('\n')[1:]] for mapping in mappings]
    for mapping in mappings:
        new_seeds = []
        while len(seeds) > 0:
            run_one_seed(mapping, new_seeds, seeds)
        seeds = new_seeds
    return min(min(seeds))


def run_one_seed(mapping, new_seeds, seeds):
    start, end = seeds.pop()
    for dest, src, length in mapping:
        overlap_start = max(start, src)
        overlap_end = min(end, src + length)
        if overlap_start < overlap_end:
            new_seeds.append([overlap_start - src + dest, overlap_end - src + dest])
            if overlap_start > start:
                seeds.append([start, overlap_start])
            if overlap_end < end:
                seeds.append([overlap_end, end])
            break
    else:
        new_seeds.append([start, end])


def main():
    almanac = get_data(day=5, year=2023).split('\n\n')
    print('day 5')
    print(f'part1: {part1(almanac)}')
    print(f'part2: {part2(almanac)}')


if __name__ == '__main__':
    main()
