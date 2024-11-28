from collections import defaultdict, deque

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

class Constellation:
    def __init__(self, input):
        self.stars = set()
        for r, row in enumerate([x.strip() for x in input.split("\n")]):
            for c, ch in enumerate(row):
                if ch != '.':
                    self.stars.add((r, c))

        self.dists = defaultdict(dict)

        for s in self.stars:
            for s2 in self.stars:
                self.dists[s][s2] = self.man_dist(s, s2)

    def man_dist(self, a: tuple[int, int], b: tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_shortest_graph(self, start) -> int:
        total = 0

        queue = deque([(start, start, 0)])
        seen = set()

        while queue:
            start, end, progress = queue.popleft()

            if end in seen:
                continue

            if self.dists[start][end] < progress:
                queue.append((start, end, progress + 1))
                continue
            else:
                seen.add(end)
                total += self.dists[start][end]
                for dest in self.dists[end].keys():
                    queue.append((end, dest, 0))

        assert len(seen) == len(self.stars)
        return total

    def __repr__(self):
        return f"{self.stars}"


def part1(input: str) -> int:
    constellation = Constellation(input)
    shortest = min([constellation.find_shortest_graph(s) for s in constellation.stars])
    return shortest

def part2(input: str) -> int:
    return 0

def part3(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















