def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data


def part1(data):
    matrix = {}
    santaX = 0
    santaY = 0
    matrix[santaX, santaY] = 1

    for c in data:
        if c == '^':
            santaY += 1
        elif c == 'v':
            santaY -= 1
        elif c == '>':
            santaX += 1
        elif c == '<':
            santaX -= 1

        try:
            matrix[santaX, santaY] += 1
        except KeyError:
            matrix[santaX, santaY] = 1

    return len(matrix)


def part2(data):
    matrix = {}
    santaX = 0
    santaY = 0
    matrix[santaX, santaY] = 1

    robotX = 0
    robotY = 0

    i = 0
    for c in data:
        i += 1
        if i % 2 == 0:
            if c == '^':
                santaY += 1
            elif c == 'v':
                santaY -= 1
            elif c == '>':
                santaX += 1
            elif c == '<':
                santaX -= 1

            try:
                matrix[santaX, santaY] += 1
            except KeyError:
                matrix[santaX, santaY] = 1

        else:
            if c == '^':
                robotY += 1
            elif c == 'v':
                robotY -= 1
            elif c == '>':
                robotX += 1
            elif c == '<':
                robotX -= 1

            try:
                matrix[robotX, robotY] += 1
            except KeyError:
                matrix[robotX, robotY] = 1

    return len(matrix)

data = loadInput()

assert part1('>') == 2
assert part1('^>v<') == 4
assert part1('^v^v^v^v^v') == 2

assert part2('^v') == 3
assert part2('^>v<') == 3
assert part2('^v^v^v^v^v') == 11

print 'Part1 is {0}'.format(str(part1(data[0])))
print 'Part2 is {0}'.format(str(part2(data[0])))
