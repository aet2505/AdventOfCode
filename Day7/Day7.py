import re


def loadInput():
    with open('input.txt', 'r') as f:
        data = f.readlines()
    return data


regexSetExtract = re.compile(r'(\w+) -> (\w+)')
regexExtract = re.compile(r'(\w+) ([A-Z]+) (\w+) -> ([a-z]{1,2})')
regexExtractNot = re.compile(r'(NOT) (\w+) -> ([a-z]{1,2})')


def getValue(matrix, key):
    if is_number(key):
        return int(key)
    return matrix[key]


def valueKnown(matrix, key):
    if is_number(key):
        return True
    return key in matrix


def is_number(s):
    return type(s) is int or s.isdigit()


def handle(data, matrix):
    while True:
        processed = False
        for command in data:
            command = str.replace(command, '\n', '')
            length = len(str(command).split(' '))
            if length == 3:
                search = regexSetExtract.search(command)
                extract = search.groups()
                action = 'SET'
                target = extract[1]
                value = 0
                input = extract[0]

            elif length == 4:
                search = regexExtractNot.search(command)
                extract = search.groups()
                input = extract[1]
                target = extract[2]
                action = extract[0]
                value = 0
            else:
                search = regexExtract.search(command)
                try:
                    extract = search.groups()
                except AttributeError:
                    print command
                action = extract[1]
                input = extract[0]
                value = extract[2]
                target = extract[3]

            if valueKnown(matrix, target):
                continue
            if not valueKnown(matrix, input) or not valueKnown(matrix, value):
                continue

            processed = True
            try:
                if action == 'AND':
                    matrix[target] = (getValue(matrix, input) & getValue(matrix, value)) % 65536
                elif action == 'OR':
                    matrix[target] = (getValue(matrix, input) | getValue(matrix, value)) % 65536
                elif action == 'LSHIFT':
                    matrix[target] = (getValue(matrix, input) << int(value)) % 65536
                elif action == 'RSHIFT':
                    matrix[target] = (getValue(matrix, input) >> int(value)) % 65536
                elif action == 'NOT':
                    matrix[target] = (~ getValue(matrix, input)) % 65536
                elif action == 'SET':
                    matrix[target] = getValue(matrix, input)
            except KeyError:
                return matrix

        if not processed:
            break
    return matrix


data = loadInput()

part_ = handle(
    ['123 -> x', '456 -> y', 'x AND y -> d', 'x OR y -> e', 'x LSHIFT 2 -> f', 'y RSHIFT 2 -> g', 'NOT x -> h',
     'NOT y -> i'], {})
print part_
assert part_['d'] == 72
assert part_['e'] == 507
assert part_['f'] == 492
assert part_['g'] == 114
assert part_['h'] == 65412
assert part_['i'] == 65079
assert part_['x'] == 123
assert part_['y'] == 456

# assert part2('') == 0
part_1 = handle(data, {})
print 'Part1 is {0}'.format(str(part_1['a']))
part_2 = handle(data, {'b': part_1['a']})
print 'Part2 is {0}'.format(str(part_2['a']))
