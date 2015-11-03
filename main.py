__author__ = 'Anton'

from itertools import combinations
from time import time

# Define files
fin = open('input')
fout = open('output.txt', 'w+')

# Define input data
cases = int(fin.readline())
result = []

for case in range(cases):
    sT = time()
    amountOfCandies = int(fin.readline())
    weightsOfCandies = fin.readline()
    weightsOfCandies = list(map(int, weightsOfCandies.split()))
    maximHappyStack = 0

    for i in range(1, round(amountOfCandies / 2) + 1):
        # A little cheat  :) But bottleneck
        stacksOfCandies = combinations(weightsOfCandies, i)

        for firstStack in stacksOfCandies:
            secondStack = weightsOfCandies.copy()
            for j in (list(firstStack)):
                secondStack.remove(j)

            # Count stacks for Sasha and Maxim
            sashaFirstStack = 0
            maximFirstStack = 0
            sashaSecondStack = 0
            maximSecondStack = 0
            for j in firstStack:
                sashaFirstStack ^= j
                maximFirstStack += j
            for j in secondStack:
                sashaSecondStack ^= j
                maximSecondStack += j

            # Compare stacks for Sasha
            if sashaFirstStack == sashaSecondStack:
                if maximSecondStack > maximFirstStack and maximSecondStack > maximHappyStack:
                    maximHappyStack = maximSecondStack
                elif maximFirstStack > maximHappyStack:
                    maximHappyStack = maximFirstStack

    if maximHappyStack is 0:
        maximHappyStack = 'NO'

    result.append('Case #{}: {}'.format(case, maximHappyStack))
    print("--- Case %s seconds ---" % (time() - sT))
fout.write('\n'.join(result))

# Close file when we done
fin.close()
fout.close()
