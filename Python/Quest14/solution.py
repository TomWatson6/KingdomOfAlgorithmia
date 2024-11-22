from collections import deque

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def man_dist(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2])

def draw(ins: list[str]) -> tuple[set[tuple[int, int, int]], tuple[int, int, int]]:
    curr = (0, 0, 0)
    seen = set()

    for i in ins:
        dir, mag = i[0], int(i[1:])

        for _ in range(mag):
            match dir:
                case 'U':
                    curr = (curr[0] + 1, curr[1], curr[2])
                case 'D':
                    curr = (curr[0] - 1, curr[1], curr[2])
                case 'L':
                    curr = (curr[0], curr[1] - 1, curr[2])
                case 'R':
                    curr = (curr[0], curr[1] + 1, curr[2])
                case 'F':
                    curr = (curr[0], curr[1], curr[2] + 1)
                case 'B':
                    curr = (curr[0], curr[1], curr[2] - 1)

            seen.add(curr)

    return (seen, curr)

def path(grid: set[tuple[int, int, int]], start: tuple[int, int, int], end: tuple[int, int, int]) -> int:
    Q = deque([(start, 0)])
    S = set()

    while Q:
        curr, depth = Q.popleft()
        r, c, d = curr

        if curr in S:
            continue

        S.add(curr)

        if curr == end:
            return depth
        
        for dr, dc, dd_ in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
            rr = r + dr
            cc = c + dc
            dd = d + dd_

            if (rr, cc, dd) in grid:
                Q.append(((rr, cc, dd), depth + 1))

    return 0

def part1(input: str) -> int:
    plant, _ = draw(input.split(","))

    low = min(x[0] for x in plant)
    high = max(x[0] for x in plant)

    return high - low + 1

def part2(input: str) -> int:
    lines = [x.strip() for x in input.split("\n")]
    final = set()

    for line in lines:
        plant, _ = draw(line.split(","))
        final = final.union(plant)

    return len(final)

def part3(input: str) -> int:
    lines = [x.strip() for x in input.split("\n")]
    final = set()
    leaves = set()

    for line in lines:
        plant, leaf = draw(line.split(","))
        final = final.union(plant)
        leaves.add(leaf)

    height = max(int(line.split(",")[0][1:]) for line in lines)

    smallest = int(1e20)

    for i in range(1, height + 1):
        a = (i, 0, 0)
        murkiness = 0
        for leaf in leaves:
            dist = path(final, a, leaf)
            murkiness += dist

        smallest = min(smallest, murkiness)

    return smallest


if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















