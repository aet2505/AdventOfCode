def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data

def part1(data):
    floor = 0
    for c in data:
        if c == ')':
            floor -= 1
        elif c == '(':
            floor += 1

    return floor

def part2(data):
    floor = 0
    index = 0
    for c in data:
        index += 1
        if c == ')':
            floor -= 1
        elif c == '(':
            floor += 1

        if floor < 0:
            return index

data = loadInput()

assert part1('(())') == 0
assert part1('(()(()(') == 3
assert part1('))(((((') == 3
assert part1('))(') == -1
assert part1(')())())') == -3

assert part2(')') == 1
assert part2('()())') == 5

print 'Floor is {0}'.format(str(part1(data[0])))
print 'First Entered Basement at action {0}'.format(str(part2(data[0])))



