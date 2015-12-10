import re


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data


badRegex = re.compile(r'(ab|cd|pq|xy)')
repeatedCharRegex = re.compile(r'((\w)\2)')
vowelRegex = re.compile(r'([aeiou])')


def part1(data):
    goodCount = 0
    for word in data:
        m = badRegex.findall(word)
        if len(m) != 0:
            continue

        m = repeatedCharRegex.findall(word)
        if len(m) == 0:
            continue

        m = vowelRegex.findall(word)
        if len(m) < 3:
            continue

        goodCount += 1

    return goodCount


repeatedPairRegex = re.compile(r'((\w{2}).*\2)')
repeatedCharSeparatedRegex = re.compile(r'((\w).\2)')


def part2(data):
    goodCount = 0
    for word in data:
        m = repeatedPairRegex.findall(word)
        if len(m) == 0:
            continue

        m = repeatedCharSeparatedRegex.findall(word)
        if len(m) == 0:
            continue

        goodCount += 1

    return goodCount


data = loadInput()

assert part1(['ugknbfddgicrmopn']) == 1
assert part1(['aaa']) == 1
assert part1(['jchzalrnumimnmhp']) == 0
assert part1(['haegwjzuvuyypxyu']) == 0
assert part1(['dvszwmarrgswjxmb']) == 0

assert part2(['qjhvhtzxzqqjkmpb']) == 1
assert part2(['xxyxx']) == 1
assert part2(['uurcxstgmygtbstg']) == 0
assert part2(['ieodomkazucvgmuy']) == 0

print 'Part1 is {0}'.format(str(part1(data)))
print 'Part2 is {0}'.format(str(part2(data)))
