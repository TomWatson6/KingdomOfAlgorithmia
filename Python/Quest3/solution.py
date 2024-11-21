
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

class Earth:
    def __init__(self, input):
        grid = {}
        for r, line in enumerate([x.strip() for x in input.split("\n")]):
            for c, ch in enumerate(line):
                if ch == '#':
                    grid[(r, c)] = 0

        self.grid = grid

    def get_adjacents(self, r: int, c: int) -> list[tuple[int, int]]:
        adj = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if abs(dr) == abs(dc):
                    continue

                rr = r + dr
                cc = c + dc

                adj.append((rr, cc))

        return adj

    def get_all_adjacents(self, r: int, c: int) -> list[tuple[int, int]]:
        adj = []

        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                rr = r + dr
                cc = c + dc

                adj.append((rr, cc))

        return adj

    def dig(self) -> int:
        new_grid = {}
        total = 0

        for loc in self.grid.keys():
            level = self.grid[loc]
            adj = self.get_adjacents(loc[0], loc[1])

            if all((self.grid[a] if a in self.grid else 0) >= level for a in adj):
                new_grid[loc] = level + 1
                total += 1
            else:
                new_grid[loc] = level

        self.grid = new_grid
        return total

    def dig_diag(self) -> int:
        new_grid = {}
        total = 0

        for loc in self.grid.keys():
            level = self.grid[loc]
            adj = self.get_all_adjacents(loc[0], loc[1])

            if all((self.grid[a] if a in self.grid else 0) >= level for a in adj):
                new_grid[loc] = level + 1
                total += 1
            else:
                new_grid[loc] = level

        self.grid = new_grid
        return total

    def __repr__(self):
        output = ""

        low_r = min(x[0] for x in self.grid.keys())
        high_r = max(x[0] for x in self.grid.keys())
        low_c = min(x[1] for x in self.grid.keys())
        high_c = max(x[1] for x in self.grid.keys())

        for r in range(low_r, high_r + 1):
            for c in range(low_c, high_c + 1):
                if (r, c) in self.grid:
                    output += str(self.grid[(r, c)])
                else:
                    output += '.'
            output += "\n"

        return output

def part1(input: str) -> int:
    earth = Earth(input)
    total = 0
    curr = -1

    while curr != 0:
        curr = earth.dig()
        total += curr

    return total

def part2(input: str) -> int:
    earth = Earth(input)
    total = 0
    curr = -1

    while curr != 0:
        curr = earth.dig()
        total += curr

    return total

def part3(input: str) -> int:
    earth = Earth(input)
    total = 0
    curr = -1

    while curr != 0:
        curr = earth.dig_diag()
        total += curr

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















