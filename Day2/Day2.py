def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

def parseDimension(dimension):
    lengths = dimension.split("x")

    l = int(lengths[0])
    w = int(lengths[1])
    h = int(lengths[2])
    lengths = [l, w, h]
    lengths.sort()
    return lengths

def part1(data):
    totalArea = 0

    for dimension in data:
        lengths = parseDimension(dimension)
        sides = [lengths[0] * lengths[1], lengths[0] * lengths[2], lengths[1] * lengths[2]]
        sides.sort()
        area = sides[0]
        for side in sides:
            area += side*2

        totalArea += area

    return totalArea

def part2(data):
    totalRibbon = 0

    for dimension in data:
        lengths = parseDimension(dimension)
        ribbon = lengths[0] * 2 + lengths[1] * 2 + lengths[0]*lengths[1]*lengths[2]

        totalRibbon += ribbon

    return totalRibbon

data = loadInput()

assert part1(['2x3x4']) == 58
assert part1(['1x1x10']) == 43

assert part2(['2x3x4']) == 34
assert part2(['1x1x10']) == 14

print 'Total area is {0}'.format(str(part1(data)))
print 'Total ribbon is {0}'.format(str(part2(data)))
