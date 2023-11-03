import random
import json
from spooky_bag_def import spooky_loot_bag_def

SEED_GLOBAL = 5005

random.seed()

def get_log_randint(min,max):
    value = random.randint(min,max)
    print('random value',value)
    return value

def pickup_random_item(bag):
    bag_size = len(bag["items"])
    return bag["items"][random.randint(0,bag_size-1)]
    #return bag["items"][get_log_randint(0,bag_size-1)]

def roll_for_item_in_category_with_unique_removal(categorydef):
    #empty bag should exist?
    try:
        uniqueitems = categorydef["only one drop items"]
    except KeyError:
        uniqueitems = []
    bag_size = len(categorydef["items"])
    item = categorydef["items"][random.randint(0,bag_size-1)] #raises ValueError in case of empty bag!
    if item in uniqueitems:
        try:
            categorydef["items"].remove(item)
        except ValueError:
            pass
    return item

def open_spooky_bag(bag_def):
    """rare 15, good 50, rare costumes 15"""
    maxprobnum = bag_def["probability_sum"]
    itemcategorylist = []
    for itemcategory in bag_def["items"]:
        if random.randint(1,maxprobnum) <= itemcategory["probability"]:            
            itemcategorylist.append(itemcategory)
            #loot.append(pickup_random_item(itemcategory))
    loot = [ roll_for_item_in_category_with_unique_removal(item)
             for item in itemcategorylist ]
    #print('loot', loot)
    return loot

def spooky_loot_bag_openings(number_of_bags):
    #spooky loot bag openings
    loot_history = {}
    for i in range(number_of_bags):
        loot = open_spooky_bag(spooky_loot_bag_def)
        #print(loot)
        for item in loot:
            try:
                loot_history[item] += 1
            except KeyError:
                loot_history[item] = 1
    #print(len(loot_history),loot_history)
    return loot_history

if False:
    inventory = spooky_loot_bag_openings(300)
    for item in inventory:
        print(item,inventory[item])

if False:
    random.seed()
    while True:
        print("opening bag...")
        print(open_spooky_bag(spooky_loot_bag_def))
        z = input()

"""
case 3: open bags till have all rare reward, to simulate
the number of bags needed to have all rare plans:
"""
if True:
    random.seed(SEED_GLOBAL)
    wantedlist = set(spooky_loot_bag_def["items"][1]["items"])
    print(wantedlist)
    number_of_bags = 0
    while len(wantedlist)>0:
        loot = open_spooky_bag(spooky_loot_bag_def)
        #print(set(loot))
        wantedlist -= set(loot)
        number_of_bags += 1
    print('all plans at',number_of_bags,'bags opened')

"""
case 4: we have some of the plans already, how many loots are needed
    to complete collection
"""
if False:
    random.seed(SEED_GLOBAL)
    already_have = [
        "Plan: Dr. Bones (2023)",
        "Plan: Executioner Mask (2023)",
        "Plan: Half Full Pumpkin Rack"      ,
        "Plan: Happy Jack O’Lantern"        ,
        "Plan: Mobster Jack O’Lantern"      ,
        "Plan: Practice Jack O’Lantern"     ,
        "Plan: Pumpkin Rack"                ,
        "Plan: Surprised Jack O’Lantern"    ,
        "Plan: Vault Boy Jack O’Lantern"    ,
        "Plan: Vault Door Jack O’Lantern"   ,
        "Plan: Grim Reaper Vault-Boy cutout",
    ]
    wantedlist = set(spooky_loot_bag_def["items"][1]["items"])
    wantedlist -= set(already_have)
    print(wantedlist)
    number_of_bags = 0
    while len(wantedlist)>0:
        loot = open_spooky_bag(spooky_loot_bag_def)
        #print(set(loot))
        wantedlist -= set(loot)
        number_of_bags += 1
    print('all plans at',number_of_bags,'bags opened')
