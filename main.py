__author__ = 'Anton'

# Define files
fin = open('input')
fout = open('output.txt', 'w+')

# Define input data
cases = int(fin.readline())
result = []

for case in range(cases):
    amountOfCandies = int(fin.readline())
    boxOfCandies = list(map(int, fin.readline().split()))
    maximHappyStack = 0

    xorResult = 0
    for candy in boxOfCandies:
        xorResult ^= candy

    if xorResult is 0:
        boxOfCandies.sort()
        maximHappyStack = sum(boxOfCandies[1:])

    if maximHappyStack is 0:
        maximHappyStack = 'NO'

    result.append('Case #{}: {}'.format(case, maximHappyStack))
fout.write('\n'.join(result))

# Close file when we done
fin.close()
fout.close()
