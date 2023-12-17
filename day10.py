from aocd import get_data
import networkx as nx


def part1(lines):
    lines = list(map(list, lines))
    tile_to_edges = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], 'L': [(-1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)],
                     '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], 'S': [], '.': []}
    start = None
    for x, line in enumerate(lines):
        for y, cell in enumerate(line):
            if cell == 'S':
                start = (x, y)
    current = aux(tile_to_edges, lines, start)
    prev = start
    all_loop = [start, current]
    while True:
        next_node = aux2(prev, current, lines, tile_to_edges)
        if next_node == start:
            break
        all_loop.append(next_node)
        prev = current
        current = next_node
    return len(all_loop) // 2


def aux(tile_to_edges, lines, start):
    s_x, s_y = start
    next_to_start = [(s_x + 1, s_y), (s_x - 1, s_y), (s_x, s_y + 1), (s_x, s_y - 1)]
    for x, y in next_to_start:
        for edge_x, edge_y in tile_to_edges[lines[x][y]]:
            if (x + edge_x, y + edge_y) == start:
                return x, y


def aux2(prev, current, lines, tile_to_edges):
    x, y = current
    for edge_x, edge_y in tile_to_edges[lines[x][y]]:
        if (x + edge_x, y + edge_y) != prev:
            return x + edge_x, y + edge_y


def part2(lines):
    return lines


def main():
    lines = get_data(day=10, year=2023).splitlines()
    print('day 10')
    print(f'part1: {part1(lines)}')
    print(f'part2: {part2(lines)}')


if __name__ == '__main__':
    main()
