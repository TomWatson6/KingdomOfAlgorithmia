
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

W = []
S = []

def parse_input(input: str):
    global W, S
    W = input.split("\n")[0].strip().split(":")[1].split(",")
    S = [s.strip() for s in input.split("\n")[2:]]

def part1(input: str) -> int:
    parse_input(input)

    total = 0

    for w in W:
        parts = len(S[0].split(w))
        total += parts - 1

    return total


def part2(input: str) -> int:
    parse_input(input)

    symbols: set[tuple[int, int, str]] = set()

    for w in W + [t[::-1] for t in W]:
        for t, s in enumerate(S):
            symbols = symbols.union(check(-1, t, s, w, False))

    return len(symbols)

def part3(input: str) -> int:
    parse_input(input)

    symbols: set[tuple[int, int, str]] = set()

    for w in W + [t[::-1] for t in W]:
        # Horizontal sentences
        for t, s in enumerate(S):
            symbols = symbols.union(check(-1, t, s, w, True))

        # Vertical sentences
        v_sentences = ["".join(S[x][s] for x in range(len(S))) for s in range(len(S[0]))]
        print(w, v_sentences)
        for t, s in enumerate(v_sentences):
            symbols = symbols.union(check(t, -1, s, w, True))

    return len(symbols)

def check(h_index: int, v_index: int, sentence: str, runic_word: str, p3: bool) -> set[tuple[int, int, str]]:
    symbols = set()
    r = len(sentence) + len(runic_word) if p3 and h_index == -1 else len(sentence)

    for i in range(r):
        # if v_index == -1 and p3:
        #     print(sentence[i % len(sentence)], end='')
        if i >= len(sentence):
            syms = sentence[i:] + sentence[:(i + len(runic_word)) % len(sentence) + 1]
        else:
            syms = sentence[i:i+len(runic_word)]

        if i + len(syms) > len(sentence) and v_index == -1:
            continue
        if "".join(syms) == runic_word:
            for j, sym in enumerate(syms):
                if h_index == -1:
                    symbols.add((v_index, (i % len(sentence)) + j, sym))
                else:
                    symbols.add(((i % len(sentence)) + j, h_index, sym))

    # if v_index == -1 and p3:
    #     exit(0)

    return symbols

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















