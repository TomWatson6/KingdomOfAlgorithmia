
input = open("input.txt").read().strip()
input2 = open("input2.txt").read().strip()
input3 = open("input3.txt").read().strip()

words = []
sentence = ""
sentences = []

def parse_input(input):
    global words, sentence
    words = []
    sentence = ""
    sentences = []

    lines = input.splitlines()
    words = lines[0].split(":")[1].split(",")
    sentence = lines[2]

def parse_input2(input):
    global words, sentences
    words = []
    sentence = ""
    sentences = []

    lines = input.splitlines()
    words = lines[0].split(":")[1].split(",")

    for sentence in lines[2:]:
        sentences.append(sentence)

def part1(input):
    parse_input(input)

    return check()

def check():
    total = 0

    for word in words:
        for i in range(len(sentence) - len(word)):
            part = sentence[i:i+len(word)]
            if word == part:
                total += 1

    return total

def part2(input):
    parse_input2(input)

    return check2()

def check2():
    found = set()

    for s, sen in list(enumerate(sentences)):
        for word in words + [w[::-1] for w in words]:
            for i in range(len(sen) - len(word) + 1):
                part = sen[i:i+len(word)]
                if word == part:
                    for j in range(len(word)):
                        found.add((s, i + j))

    return len(found)

def part3(input):
    parse_input2(input)

    return check3()

def check3():
    found = set()

    for s, sen in list(enumerate(sentences)):
        for word in words + [w[::-1] for w in words]:
            for i in range(len(sen)):
                left = i
                right = (i + len(word)) % len(sen)
                part = ""

                if right < left:
                    part = sen[left:] + sen[:right]
                else:
                    part = sen[left:right]

                if word == part:
                    for j in range(len(word)):
                        found.add((s, (i + j) % len(sen)))


    for s, sen in enumerate(list("".join(x) for x in list(zip(*sentences)))):
        for word in words + [w[::-1] for w in words]:
            for i in range(len(sen) - len(word) + 1):
                part = sen[i:i + len(word)]
                if word == part:
                    for j in range(len(word)):
                        found.add((i + j, s))

    return len(found)

if __name__ == "__main__":
    print("Part 1:", part1(input))
    print("Part 2:", part2(input2))
    print("Part 3:", part3(input3))

















