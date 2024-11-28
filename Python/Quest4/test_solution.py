
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def part1(input: str) -> int:
    nums = [int(x.strip()) for x in input.split("\n")]
    smallest = min(nums)

    return sum(n - smallest for n in nums)

def part2(input: str) -> int:
    nums = [int(x.strip()) for x in input.split("\n")]
    smallest = min(nums)

    return sum(n - smallest for n in nums)

def part3(input: str) -> int:
    nums = [int(x.strip()) for x in input.split("\n")]
    mean = float(sum(nums)) / len(nums)
    mean = int(mean + 1.5)

    return sum(abs(n - mean) for n in nums)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















