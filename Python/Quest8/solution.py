
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

def part1(input: str) -> int:
    width = 1 # current width of the pyramid
    curr = 1 # total number of blocks in pyramid
    addition = 3 # number to keep track of how many blocks are required for next instalment
    final = int(input)

    while curr + addition < final:
        curr += addition
        addition += 2
        width += 2

    width += 2

    return (curr + addition - final) * width


def part2(input: str) -> int:
    return 0

def part3(input: str) -> int:
    return 0

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















