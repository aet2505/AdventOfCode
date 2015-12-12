import re
from json import loads


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

regexExtractNumber = re.compile(r'(-?\d+)')

def part1(data):
    total = 0
    for x in regexExtractNumber.findall(data):
        total += int(x)

    return total


def part2(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum([part2(entry) for entry in data])
    if type(data) != dict:
        return 0
    if 'red' in data.values():
        return 0
    return part2(list(data.values()))

data = loadInput()

print 'Part1 is {0}'.format(str(part1(data[0])))
print 'Part2 is {0}'.format(str(part2(loads(data[0]))))



