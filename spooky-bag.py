import random
import json
from spooky_bag_def import spooky_loot_bag_def

SEED_GLOBAL = 5004045

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
            #itemcategorylist.append(itemcategory)
            itemcategorylist += [itemcategory]
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

if True:
    random.seed(SEED_GLOBAL)
    inventory = spooky_loot_bag_openings(300)
    print('different items get',len(inventory))
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
if False:
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
if True:
    random.seed(SEED_GLOBAL)
    already_have = [
        "Plan: Assault Rifle Wraith's Wrath Paint (2023)",
        "Plan: Chainsaw Ghostly Grinder Paint (2023)",
        "Plan: Dr. Bones (2023)",
        "Plan: Executioner Mask (2023)",
        "Plan: Hellfire V2 Prototype PA Arms Paint (2023)",
        "Plan: Hellfire V2 Prototype PA Helmet Paint (2023)",
        "Plan: Hellfire V2 Prototype PA Legs Paint (2023)",
        "Plan: Hellfire V2 Prototype PA Torso Paint (2023)",
        "Plan: Honeycomb Paper Ghost Lantern 01 (2023)",
        "Plan: Honeycomb Paper Ghost Lantern 02 (2023)",
        "Plan: Honeycomb Paper Jack-o'-Lantern 01 (2023)",
        "Plan: Honeycomb Paper Jack-o'-Lantern 02 (2023)",
        "Plan: Honeycomb Paper Spider Lantern (2023)",
        "Plan: Princess Backpack (2023)",
        "Plan: Rad Skull Rider Helmet (2023)"
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
