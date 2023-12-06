from itertools import batched

from aocd import get_data


def part1(almanac):
    seeds = list(map(int, almanac[0].split()[1:]))
    mappings = almanac[1:]
    mappings = [[[int(y) for y in x.split()] for x in mapping.split('\n')[1:]] for mapping in mappings]
    location_numbers = []
    for seed in seeds:
        src = seed
        for mapping in mappings:
            src = get_dest_value(src, mapping)
        location_numbers.append(src)
    return min(location_numbers)


def get_dest_value(src, mapping):
    for map_range in mapping:
        dest_start, src_start, length = map_range
        if src_start <= src < src_start + length:
            return src + (dest_start - src_start)
    return src


def part2(almanac):
    seeds = list(map(int, almanac[0].split()[1:]))
    seeds = [[x, x + y - 1] for x, y in batched(seeds, 2)]
    mappings = almanac[1:]
    mappings = [[[int(y) for y in x.split()] for x in mapping.split('\n')[1:]] for mapping in mappings]
    location_numbers = []
    for seed in seeds:
        src_ranges = [seed]
        for mapping in mappings:
            dest_ranges = []
            for src_range in src_ranges:
                dest_ranges += get_dest_value2_aux(src_range, mapping)
            src_ranges = dest_ranges
        location_numbers += src_ranges
    return min(min(location_numbers))


def get_dest_value2_aux(original, mapping):
    if mapping:
        dest, originals = get_dest_value2(original, mapping[0])
        if originals:
            for org in originals:
                dest += get_dest_value2_aux(org, mapping[1:])
        return dest
    else:
        return [original]


def get_dest_value2(src, map_range):
    src_start, src_end = src
    map_dest_start, map_src_start, map_length = map_range
    map_src_end = map_src_start + map_length - 1
    dest = []
    original = []
    offset = map_dest_start - map_src_start
    if src_start < map_src_start:
        if src_end < map_src_start:
            # ss+se ms-me
            original.append([src_start, src_end])
        elif src_end <= map_src_end:
            # ss+ms+se-me
            original.append([src_start, map_src_start - 1])
            dest.append([map_dest_start, src_end + offset])
        else:
            # ss+ms+me+se
            original.append([src_start, map_src_start - 1])
            dest.append([map_dest_start, map_dest_start + map_length - 1])
            original.append([map_src_end + 1, src_end])
    else:
        if src_start > map_src_end:
            # ms-me ss+se
            original.append([src_start, src_end])
        elif src_end > map_src_end:
            # ms-ss+me+se
            dest.append([src_start + offset, map_dest_start + map_length - 1])
            original.append([map_src_end + 1, src_end])
        else:
            # ms-ss+se-me
            dest.append([src_start + offset, src_end + offset])
    return dest, original


def main():
    almanac = get_data(day=5, year=2023).split('\n\n')
    print('day 5')
    print(f'part1: {part1(almanac)}')
    print(f'part2: {part2(almanac)}')


if __name__ == '__main__':
    main()
