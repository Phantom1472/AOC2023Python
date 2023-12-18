from aocd import get_data


def part1(lines):
    lines = list(map(list, lines))
    loop = get_loop(lines)
    return len(loop) // 2


def part2(lines):
    lines: list[list[str]] = list(map(list, lines))
    loop = get_loop(lines)
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell == 'S':
                lines[x][y] = '7'  # specific to my input
    total_inner = 0
    corner_parts = {'L', 'J', 'F', '7'}
    for x, line in enumerate(lines):
        inside_loop_flag = False
        last_corner = None
        for y, cell in enumerate(line):
            if (x, y) in loop:
                if cell == '|':
                    inside_loop_flag = not inside_loop_flag
                elif cell in corner_parts:
                    if last_corner:
                        if {last_corner, cell} not in [{'L', 'J'}, {'F', '7'}]:
                            inside_loop_flag = not inside_loop_flag
                        last_corner = None
                    else:
                        last_corner = cell
            else:
                if inside_loop_flag:
                    total_inner += 1
    return total_inner


def get_loop(lines):
    tile_to_edges = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
                     '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], 'S': [], '.': []}
    start = None
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell == 'S':
                start = (x, y)
    current = get_next_to_start(tile_to_edges, lines, start)
    prev = start
    all_loop = [start, current]
    while True:
        next_node = get_next(prev, current, lines, tile_to_edges)
        if next_node == start:
            break
        all_loop.append(next_node)
        prev = current
        current = next_node
    return all_loop


def get_next_to_start(tile_to_edges, lines, start):
    s_x, s_y = start
    next_to_start = [(s_x + 1, s_y), (s_x - 1, s_y), (s_x, s_y + 1), (s_x, s_y - 1)]
    for x, y in next_to_start:
        for edge_x, edge_y in tile_to_edges[lines[x][y]]:
            if (x + edge_x, y + edge_y) == start:
                return x, y


def get_next(prev, current, lines, tile_to_edges):
    x, y = current
    for edge_x, edge_y in tile_to_edges[lines[x][y]]:
        if (x + edge_x, y + edge_y) != prev:
            return x + edge_x, y + edge_y


def main():
    lines = get_data(day=10, year=2023).splitlines()
    print('day 10')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
