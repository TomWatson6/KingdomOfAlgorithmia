from collections import deque

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def path(start: tuple[int, int], dest: tuple[int, int], grid: dict[tuple[int, int], int]) -> int:
    Q = deque([(start, 0, 0)])
    seen = set()

    while Q:
        loc, time, depth = Q.popleft()
        r, c = loc

        if loc == dest:
            return depth

        if (loc, time) in seen:
            continue

        seen.add((loc, time))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] != '#':
                if grid[(rr, cc)] == (grid[loc] + time) % 10 or grid[(rr, cc)] == (grid[loc] - time) % 10:
                    Q.append(((rr, cc), 0, depth + 1))
                else:
                    Q.append((loc, time + 1, depth + 1))

    return 0

def path2(start: tuple[int, int], ends: list[tuple[int, int]], grid: dict[tuple[int, int], int]) -> int:
    Q = deque([(start, 0, 0)])
    seen = set()

    while Q:
        loc, time, depth = Q.popleft()
        r, c = loc

        if loc in ends:
            return depth

        if (loc, time) in seen:
            continue

        seen.add((loc, time))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in grid and grid[(rr, cc)] != '#':
                if grid[(rr, cc)] == (grid[loc] + time) % 10 or grid[(rr, cc)] == (grid[loc] - time) % 10:
                    Q.append(((rr, cc), 0, depth + 1))
                else:
                    Q.append((loc, time + 1, depth + 1))

    return 0

def get_grid(input: str) -> tuple[dict[tuple[int, int], int], int, int]:
    lines = [x.strip() for x in input.split("\n")]
    grid = {}
    start = (0, 0)
    end = (0, 0)

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == 'S':
                start = (r, c)
                grid[(r, c)] = 0
            elif ch == 'E':
                end = (r, c)
                grid[(r, c)] = 0
            elif ch == '#':
                grid[(r, c)] = ch
            elif ch == ' ':
                continue
            else:
                grid[(r, c)] = int(ch)

    return grid, start, end

def get_grid2(input: str) -> tuple[dict[tuple[int, int], int], list[int], int]:
    lines = [x.strip() for x in input.split("\n")]
    grid = {}
    start = []
    end = (0, 0)

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch == 'S':
                start.append((r, c))
                grid[(r, c)] = 0
            elif ch == 'E':
                end = (r, c)
                grid[(r, c)] = 0
            elif ch == '#':
                grid[(r, c)] = ch
            elif ch == ' ':
                continue
            else:
                grid[(r, c)] = int(ch)

    return grid, start, end

def part1(input: str) -> int:
    grid, start, end = get_grid(input)

    dist = path(start, end, grid)

    return dist

def part2(input: str) -> int:
    grid, start, end = get_grid(input)

    dist = path(start, end, grid)

    return dist

def part3(input: str) -> int:
    grid, ends, start = get_grid2(input)

    dist = path2(start, ends, grid)

    return dist

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















