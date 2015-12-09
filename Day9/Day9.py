from itertools import permutations
import re

import sys

extractParts = re.compile(r'(\w+) to (\w+) = ([0-9]+)')


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data


def parse(data):
    dests = set()
    distances = {}
    shortest = sys.maxint
    longest = 0

    extractData(data, dests, distances)

    for perm in permutations(dests):
        fromLoc = None
        dist = 0
        for loc in perm:
            if fromLoc is None:
                fromLoc = loc
                continue
            else:
                dist += distances[fromLoc][loc]
                fromLoc = loc
        shortest = min(shortest, dist)
        longest = max(longest, dist)
    print "Shortest is {0}".format(str(shortest))
    print "Longest is {0}".format(str(longest))


def extractData(data, dests, distances):
    for line in data:
        parts = extractParts.search(line).groups()
        dests.add(parts[0])
        dests.add(parts[1])

        if parts[0] not in distances:
            distances[parts[0]] = {}
        if parts[1] not in distances:
            distances[parts[1]] = {}

        distances[parts[0]][parts[1]] = int(parts[2])
        distances[parts[1]][parts[0]] = int(parts[2])


data = loadInput()
parse(data)
