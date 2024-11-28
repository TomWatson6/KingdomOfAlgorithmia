import itertools
from collections import deque

input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()
track = open("race_track.txt").read().strip()
track2 = open("race_track2.txt").read().strip()

def parse_race_track(input: str) -> list[str]:
    lines = [x.strip() for x in input.split("\n")]

    G = {}

    for r, line in enumerate(lines):
        for c, ch in enumerate(line):
            if ch != ' ':
                G[(r, c)] = ch

    race_track = [G[(0, 1)]]

    Q = deque([(0, 2)])
    S = set()
    S.add((0, 1))

    while Q:
        r, c = Q.popleft()

        if (r, c) in S:
            continue
        
        S.add((r, c))

        race_track.append(G[(r, c)])

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            rr = r + dr
            cc = c + dc

            if (rr, cc) in G:
                Q.append((rr, cc))

    return race_track

    # for c in range(1, len(lines[0])):
    #     race_track.append(lines[0][c])

    # for r in range(1, len(lines)):
    #     race_track.append(lines[r][len(lines[0]) - 1])

    # for c in range(len(lines[0]) - 2, -1, -1):
    #     race_track.append(lines[len(lines) - 1][c])

    # for r in range(len(lines) - 2, -1, -1):
    #     race_track.append(lines[r][0])

class Device:
    def __init__(self, line: str):
        name, config = line.split(":")
        self.name = name
        self.config = config.split(",")
        self.power = 10
        self.pointer = 0
        self.points = 0

    def inc_pointer(self):
        self.pointer = (self.pointer + 1) % len(self.config)

    def adjust(self):
        match self.config[self.pointer]:
            case '+':
                self.power += 1
            case '-':
                self.power -= 1
            case _:
                pass
        self.points += self.power
        self.inc_pointer()

    def adjust2(self, race_track: list[str], race_pointer: int):
        match race_track[race_pointer % len(race_track)]:
            case '+':
                self.power += 1
                self.points += self.power
                self.inc_pointer()
            case '-':
                self.power -= 1
                self.points += self.power
                self.inc_pointer()
            case _:
                self.adjust()

    def progress(self, count: int) -> int:
        for _ in range(count):
            self.adjust()

        return self.points

    def progress2(self, count: int, race_track: list[str], race_pointer: int) -> int:
        skippable = False

        if len(race_track) % len(self.config) == 0:
            skippable = True

        for i in range(count * len(race_track)):
            if i == len(race_track):
                rem_cycles = count - 1
                power_diff = self.power - 10

                return self.pointer * count
            self.adjust2(race_track, race_pointer)
            race_pointer += 1

        return self.points

def part1(input: str) -> int:
    lines = [x.strip() for x in input.split("\n")]
    devices = [Device(line) for line in lines]
    ranks = {d.name: d.progress(10) for d in devices}
    D = ranks.keys()
    D = sorted(D, key=lambda k: ranks[k])[::-1]

    return "".join(D)

def part2(input: str, track: str) -> int:
    lines = [x.strip() for x in input.split("\n")]
    devices = [Device(line) for line in lines]
    ranks = {}

    for device in devices:
        race_track = parse_race_track(track)
        ptr = 0
        rank = device.progress2(10, race_track, ptr)
        ranks[device.name] = rank

    D = ranks.keys()
    D = sorted(D, key=lambda k: ranks[k])[::-1]

    return "".join(D)


def part3(input: str, track: str) -> int:
    config = ['+'] * 5 + ['-'] * 3 + ['='] * 3
    # print(len(list(itertools.permutations(config))))
    knight = Device(input)
    race_track = parse_race_track(track)
    score = knight.progress2(2024, race_track, 0)

    winners = 0

    for i, p in enumerate(itertools.permutations(config)):
        d = Device("t:" + ",".join(p))
        s = d.progress2(2024, race_track, 0)
        if s > score:
            winners += 1

        if i % 1000 == 0:
            print(i)

    return winners

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2, track))
    print("Part 3:", part3(input3, track2))

















