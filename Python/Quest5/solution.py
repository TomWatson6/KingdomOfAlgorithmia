from collections import defaultdict

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

class Columns:
    def __init__(self, nums: list[list[int]]):
        self.index = 0
        self.columns = nums
    
    def evolve(self) -> int:
        clapper = self.columns[self.index % len(self.columns)].pop(0)
        focused = self.columns[(self.index + 1) % len(self.columns)]

        if clapper <= len(focused):
            focused.insert(clapper - 1, clapper)
        else:
            focused.insert(len(focused) - (clapper - len(focused)), clapper)

        self.columns[(self.index + 1) % len(self.columns)] = focused

        self.index += 1

        return int("".join([str(a) for a in [x[0] for x in self.columns]]))

    def __repr__(self):
        return str(self.columns)

def parse_columns(input: str) -> Columns:
    lines = [x.strip() for x in input.split("\n")]
    lines = [[int(y) for y in x.split(" ")] for x in lines]

    columns = [[lines[r][c] for r in range(len(lines))] for c in range(len(lines[0]))]
    return Columns(columns)

def part1(input: str) -> int:
    columns = parse_columns(input)
    ans = 0

    for i in range(10):
        ans = columns.evolve()

    return ans

def part2(input: str) -> int:
    columns = parse_columns(input)
    found_at = defaultdict(int)
    rounds = 0

    while True:
        ans = columns.evolve()
        rounds += 1
        if ans not in found_at:
            found_at[ans] += rounds
        else:
            cycle = rounds - found_at[ans]
            cycle *= 2022
            rounds += cycle
            return rounds * ans

    print([k for k, v in counts.items() if v == 2024])
    return rounds * [k for k, v in counts.items() if v == 2024][0]

def part3(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















