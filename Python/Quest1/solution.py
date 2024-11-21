
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

P = {
    'A': 0,
    'B': 1,
    'C': 3,
    'D': 5,
}

N = {
    0: 0,
    1: 0,
    2: 2,
    3: 6,
}

def part1(input: str) -> int:
    return sum([P[x] for x in input])

def part2(input: str) -> int:
    total = 0

    for i in range(0, len(input), 2):
        creatures = input[i], input[i + 1]
        num_creatures = sum(1 if c in P else 0 for c in creatures)
        total += sum(P[x] if x in P else 0 for x in creatures)
        total += N[num_creatures]

    return total

def part3(input: str) -> int:
    total = 0

    for i in range(0, len(input), 3):
        creatures = input[i], input[i + 1], input[i + 2]
        num_creatures = sum(1 if c in P else 0 for c in creatures)
        total += sum(P[x] if x in P else 0 for x in creatures)
        total += N[num_creatures]

    return total

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















