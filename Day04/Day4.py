import hashlib


def loadInput():
    return 'iwrupvqb'


def part1(data):
    key = 0

    while True:
        temp = data + str(key)
        md5 = hashlib.md5()
        md5.update(temp)
        hex = md5.hexdigest()

        if hex[:5] == '00000':
            break
        else:
            key += 1

    return key

def part2(data):
    key = 0

    while True:
        temp = data + str(key)
        md5 = hashlib.md5()
        md5.update(temp)
        hex = md5.hexdigest()

        if hex[:6] == '000000':
            break
        else:
            key += 1

    return key


data = loadInput()

assert part1('abcdef') == 609043
assert part1('pqrstuv') == 1048970

print 'Part1 is {0}'.format(str(part1(data)))
print 'Part2 is {0}'.format(str(part2(data)))
