import re

regexConsecStrings = re.compile(r'([a-z])\1[a-z]*([a-z])\2')


def convertBytes(data):
    value = []
    for c in data:
        value.append(ord(c))

    return value


def convertString(data):
    value = []
    for c in data:
        value.append(chr(c))

    return ''.join(value)


def count(numberData, index):
    if numberData[index] == 122:
        numberData[index] = 97  # Reset to A
        count(numberData, index - 1)  # Count the next char
    else:
        numberData[index] += 1

    return numberData


def validPassword(data, numberData):
    if 'i' in data or 'o' in data or 'l' in data:
        return False
    if not regexConsecStrings.search(data):
        return False

    incrementingCount = 0
    previousNumber = 0
    for n in numberData:
        if n == previousNumber + 1:
            previousNumber += 1
            incrementingCount += 1
            if incrementingCount >= 3:
                return True
        else:
            previousNumber = n
            incrementingCount = 1

    return False


def generate(inputData):
    data = inputData
    numberData = convertBytes(data)
    while True:
        count(numberData, 7)
        data = convertString(numberData)
        if validPassword(data, numberData):
            return data


assert generate('abcdefgh') == 'abcdffaa'
assert generate('ghijklmn') == 'ghjaabcc'

part_1 = generate('hepxcrrq')
print 'Part1 is {0}'.format(part_1)
print 'Part2 is {0}'.format(generate(part_1))
