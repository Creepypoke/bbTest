__author__ = 'Anton'

import random

# Define files
fin = open('input', 'w+')

cases = 2
fin.write(str(cases) + '\n')
for case in range(0, cases):
    candies = random.randint(5, 25)
    fin.write(str(candies) + '\n')
    candiesWeights = []
    for c in range(0, candies):
        candyWeight = random.randint(0, 1000000)
        candiesWeights.append(str(candyWeight))
    fin.write(' '.join(candiesWeights) + '\n')
# Close file when we done
fin.close()
