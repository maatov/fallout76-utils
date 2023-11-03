"""
moleminer pails testing
dusty 10%
normal 40%
ornate 60%
"""

import random

class PailType_Dusty:
    def __init__(self):
        self.price = 219
        self.chance = 0.1
        self.name = 'Dusty'

class PailType_Normal:
    def __init__(self):
        self.price = 656
        self.chance = 0.4
        self.name = 'Normal'

class PailType_Ornate:
    def __init__(self):
        self.price = 1925
        self.chance = 0.6
        self.name = 'Ornate'

def dice_chance_throw(probability):
    return  random.uniform(0,1.0) <= probability

def arithmetic_mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def test_moleminer_chest(type_ch, maxamount=30000, verbose = False):
    #simulate openings of chest for moleminer treasure prize
    # we'll be buing chests and opening them
    prize = 0
    spent = type_ch.price
    while spent < maxamount:
        #try
        spent += type_ch.price
        prize += (1 if dice_chance_throw(type_ch.chance) else 0)
    if verbose:
        print('  spent: {}, prizes: {} '.format(spent,prize))
    return (prize,spent)

totalForSpending = 40000
types = [ PailType_Dusty(), PailType_Normal(), PailType_Ornate() ]
for ttype in types:
    suma = []
    for i in range(100):
        (a,b) = test_moleminer_chest( ttype, totalForSpending, False )
        suma.append(a)
    print('mean for {}: {}'.format(ttype.name,arithmetic_mean(suma)) )

