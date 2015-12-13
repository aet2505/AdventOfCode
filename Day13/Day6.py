import re
from itertools import permutations

import sys


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

regexExtract = re.compile(r'(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)')

def part1(data):
    people = []
    happyDelta = {}
    for entry in data:
        groups = regexExtract.search(entry).groups()
        if groups[0] not in people:
            people.append(groups[0])
        if groups[3] not in people:
            people.append(groups[3])
        delta = groups[2]
        if groups[1] == 'lose':
            delta = '-' + delta
        delta = int(delta)

        happyDelta['%s -> %s' % (groups[0], groups[3])] = delta

    maxValue = -sys.maxint - 1
    for perm in permutations(people):
        value = 0
        for i in range(0, len(perm)):
            try:
                value += happyDelta['%s -> %s' % (perm[i], perm[i+1])]
                value += happyDelta['%s -> %s' % (perm[i+1], perm[i])]
            except IndexError:
                value += happyDelta['%s -> %s' % (perm[i], perm[0])]
                value += happyDelta['%s -> %s' % (perm[0], perm[i])]
        maxValue = max(maxValue, value)

    print maxValue
    return maxValue


def part2(data):
    people = []
    happyDelta = {}
    people.append('me')
    for entry in data:
        groups = regexExtract.search(entry).groups()
        if groups[0] not in people:
            people.append(groups[0])
        if groups[3] not in people:
            people.append(groups[3])
        delta = groups[2]
        if groups[1] == 'lose':
            delta = '-' + delta
        delta = int(delta)

        happyDelta['%s -> %s' % (groups[0], groups[3])] = delta

    maxValue = -sys.maxint - 1
    for perm in permutations(people):
        value = 0
        for i in range(0, len(perm)):
            try:
                try:
                    value += happyDelta['%s -> %s' % (perm[i], perm[i+1])]
                    value += happyDelta['%s -> %s' % (perm[i+1], perm[i])]
                except IndexError:
                    value += happyDelta['%s -> %s' % (perm[i], perm[0])]
                    value += happyDelta['%s -> %s' % (perm[0], perm[i])]
            except KeyError:
                #Contains 'ME' so skip it
                continue
        maxValue = max(maxValue, value)

    print maxValue
    return maxValue

data = loadInput()

assert part1(['Alice would gain 54 happiness units by sitting next to Bob.',
              'Alice would lose 79 happiness units by sitting next to Carol.',
              'Alice would lose 2 happiness units by sitting next to David.',
              'Bob would gain 83 happiness units by sitting next to Alice.',
              'Bob would lose 7 happiness units by sitting next to Carol.',
              'Bob would lose 63 happiness units by sitting next to David.',
              'Carol would lose 62 happiness units by sitting next to Alice.',
              'Carol would gain 60 happiness units by sitting next to Bob.',
              'Carol would gain 55 happiness units by sitting next to David.',
              'David would gain 46 happiness units by sitting next to Alice.',
              'David would lose 7 happiness units by sitting next to Bob.',
              'David would gain 41 happiness units by sitting next to Carol.']) == 330

print 'Part1 is {0}'.format(str(part1(data)))
print 'Part2 is {0}'.format(str(part2(data)))



