def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

def part1(data):
    lengthDiff = 0
    for line in data:
        eval1 = eval(line[:-1])
        lengthDiff += len(line[:-1]) - len(eval1)

    return lengthDiff

def part2(data):
    lengthDiff = 0
    for line in data:
        lengthDiff += 2 #Quote marks to be added
        lengthDiff += line.count('"') #each " would need an escape
        lengthDiff += line.count('\\') #each \ would need an escape

    return lengthDiff

data = loadInput()

print 'Part1 is {0}'.format(str(part1(data)))
print 'Part2 is {0}'.format(str(part2(data)))



