#good rewards
good_rewards = {
    "name" : "good reward",
    "probability" : 50,
    "items" : [
        "Civil War Era Dress",
        "Civil War Era Suit",
        "Civil War Era Top Hat",
        "Clean Spacesuit",
        "Clown Hat",
        "Clown Outfit",
        "Fireman Helmet",
        "Fireman Uniform",
        "Golf Outfit",
        "Golf Skirt",
        "Halloween Costome Skeleton Outfit",
        "Halloween Costume Skull",
        "Halloween Costume Witch Hat",
        "Halloween Costume Witch Outfit",
        "Pastor's Vestments",
        "Plan: Cultist Blade",
        "Plan: Cultist Dagger",
        "Plan: Meat Hook",
        "Plan: Scarecrows",
        "Plan: Sickle",
        "Ranger Hat Clean ",
        "Ranger Outfit Clean ",
        "Tattered Mole Head",
        "Whitesprings Jumpsuit",
    ]
}
#rare costumes
rare_costumes = {
    "name" : "rare costume",
    "probability" : 15,
    "items" : [
        "Jack O’Lantern Pant Suit",
        "Jack O’Lantern Short Suit",
        "Pirate Costume",
        "Pirate Custome Hat",
        "Bear Gas Mask",
        "Gazelle Gas Mask",
        "Rooster Gas Mask"        
        ]
    }
    
#rare plans
rare_plans = {
    "name" : "rare plan",
    "probability" : 15,
    "items" : [
        "Plan: Grim Reaper Vault-Boy cutout",
        "Plan: Alien Jack O’Lantern"        ,
        "Plan: Classic Jack O’Lantern"      ,
        "Plan: Evil Jack O’Lantern"         ,
        "Plan: Full Pumpkin Rack"           ,
        "Plan: Half Empty Pumpkin Rack"     ,
        "Plan: Half Full Pumpkin Rack"      ,
        "Plan: Happy Jack O’Lantern"        ,
        "Plan: Mobster Jack O’Lantern"      ,
        "Plan: Practice Jack O’Lantern"     ,
        "Plan: Pumpkin Rack"                ,
        "Plan: Surprised Jack O’Lantern"    ,
        "Plan: Vault Boy Jack O’Lantern"    ,
        "Plan: Vault Door Jack O’Lantern"   ,
        "Plan: Vault-Tec Jack O’Lantern",
        "Plan: Assault Rifle Wraith's Wrath Paint (2023)",
        "Plan: Chainsaw Ghostly Grinder Paint (2023)",
        "Plan: Dr. Bones (2023)",
        "Plan: Executioner Mask (2023)",
        "Plan: Giant Red Dinosaur (2023)",
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
    ],
    "only one drop items" : [
        "Plan: Assault Rifle Wraith's Wrath Paint (2023)",
        "Plan: Chainsaw Ghostly Grinder Paint (2023)",
        "Plan: Dr. Bones (2023)",
        "Plan: Executioner Mask (2023)",
        "Plan: Giant Red Dinosaur (2023)",
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
}

def __init__():
    print("__init__()")

"""
spooky treat bag loot definition
"""
spooky_loot_bag_def = {
    "name" : "spooky_loot_bag",
    "probability_sum" : 100,
    "items" : [
        good_rewards,
        rare_plans,
        rare_costumes
        ]
    }

if False:
    import json
    s = json.dumps(spooky_loot_bag_def,indent=4)
    print(s)

