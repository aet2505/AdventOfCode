import re


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

regexExtractInfo = re.compile(r'(toggle|turn on|turn off) (\d{1,3},\d{1,3}) through (\d{1,3},\d{1,3})')
regexExtractCoord = re.compile(r'(\d{1,3}),(\d{1,3})')
grid = {}

def turnOnPart1(light):
        light.on = True

def togglePart1(light):
    light.on = not light.on

def turnOffPart1(light):
    light.on = False

class LightPart1:
    def __init__(self):
        self.on = False

    def isLit(self):
        return self.on

actionsPart1 = {
    'turn on': turnOnPart1,
    'turn off': turnOffPart1,
    'toggle': togglePart1
}

def part1(data):
    for x in range(0, 1000):
        for y in range(0, 1000):
            grid['%i,%i' % (x, y)] = LightPart1()

    for command in data:
        extract = regexExtractInfo.search(command).groups()
        coord1 = regexExtractCoord.search(extract[1]).groups()
        coord2 = regexExtractCoord.search(extract[2]).groups()
        action = actionsPart1[extract[0]]
        for x in range(int(coord1[0]), int(coord2[0])+1):
            for y in range(int(coord1[1]), int(coord2[1])+1):
                light = grid['%i,%i' % (x, y)]
                action(light)

    litCount = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            light = grid['%i,%i' % (x, y)]
            if light.isLit():
                litCount += 1

    return litCount

def turnOnPart2(light):
    light.brightness +=1

def togglePart2(light):
    light.brightness += 2

def turnOffPart2(light):
    light.brightness = max(light.brightness - 1, 0)

class LightPart2:
    def __init__(self):
        self.brightness = 0

    def getBrightness(self):
        return self.brightness

actionsPart2 = {
    'turn on': turnOnPart2,
    'turn off': turnOffPart2,
    'toggle': togglePart2
}

def part2(data):
    for x in range(0, 1000):
        for y in range(0, 1000):
            grid['%i,%i' % (x, y)] = LightPart2()

    for command in data:
        extract = regexExtractInfo.search(command).groups()
        coord1 = regexExtractCoord.search(extract[1]).groups()
        coord2 = regexExtractCoord.search(extract[2]).groups()
        action = actionsPart2[extract[0]]
        for x in range(int(coord1[0]), int(coord2[0])+1):
            for y in range(int(coord1[1]), int(coord2[1])+1):
                light = grid['%i,%i' % (x, y)]
                action(light)

    totalBright = 0
    for x in range(0, 1000):
        for y in range(0, 1000):
            light = grid['%i,%i' % (x, y)]
            totalBright += light.getBrightness()

    return totalBright

data = loadInput()
print 'Part1 is {0}'.format(str(part1(data)))
print 'Part2 is {0}'.format(str(part2(data)))



