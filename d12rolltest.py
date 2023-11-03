#special dice throw test
# we want to just 2 number from 12sided dice applying reroll technique

import random

random.seed()

def throw_dice_Dn(wanted=range(12),sides=12):
    w = set(wanted)
    while True:
        value = random.randint(1,sides)
        if value in w:
            return value
    pass

#test with 1,2 (and it really seems to be with 1/2 probability)
counts = [ 0, 0, 0 ]
iterations = 10000
for i in range(iterations):
    counts[ throw_dice_Dn([1,2],20) ] += 1
print('ratios', counts[1]/iterations, counts[2]/iterations)
