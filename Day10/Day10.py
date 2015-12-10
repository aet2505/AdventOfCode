def parse(inputData, noIterations):
    data = str(inputData)
    for i in range(0, noIterations):
        output = ''
        currentChar = None
        currentCount = 0
        for c in data:
            if currentChar is None:
                currentChar = c
                currentCount = 1
            elif currentChar is c:
                currentCount += 1
            else:
                output += str(currentCount) + currentChar
                currentChar = c
                currentCount = 1

        output += str(currentCount) + currentChar
        data = output
    return data

assert parse(1, 5) == '312211'

part_1 = str(parse(1321131112, 40))
print part_1
print 'Part1 is {0}'.format(len(part_1))

part_2 = str(parse(1321131112, 50))
print part_2
print 'Part2 is {0}'.format(len(part_2))



