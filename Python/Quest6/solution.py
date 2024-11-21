from collections import deque, defaultdict

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def parse_input(input: str) -> dict[str, list[str]]:
    lines = [x.strip() for x in input.split("\n")]
    tree = {}

    for line in lines:
        left, right = line.split(":")
        right = right.split(",")
        tree[left] = right

    return tree

def strongest(start: str, tree: dict[str, list[str]]) -> list[str]:
    paths = []
    Q = deque([(start, [])])
    seen = set()

    while Q:
        node, path = Q.popleft()

        if node in seen:
            continue

        if node != '@':
            seen.add(node)

        if node == '@':
            paths.append(path + [node])
            continue

        if node not in tree:
            continue

        for branch in tree[node]:
            Q.append((branch, path + [node]))

    counts = defaultdict(int)

    for path in paths:
        counts[len(path)] += 1

    length = [k for k, v in counts.items() if v == 1][0]
    path = [p for p in paths if len(p) == length][0]

    return path

def part1(input: str) -> int:
    tree = parse_input(input)
    apple = "".join(strongest("RR", tree))
    return apple

def part2(input: str) -> int:
    tree = parse_input(input)
    apple = "".join(x[0] for x in strongest("RR", tree))
    return apple

def part3(input: str) -> int:
    tree = parse_input(input)
    apple = "".join(x[0] for x in strongest("RR", tree))
    return apple

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















