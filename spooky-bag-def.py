#good rewards
good_rewards = {
    "probability" : 50,
    "items" : [
        "Civil War Era Dress",
        "Civil War Era Hat",
        "Civil War Era Suit",
        "Clean Ranger Outfit",
        "Clean Spacesuit Helmet",
        "Clown Hat",
        "Clown Uutfit",
        "Fireman Helmet",
        "Fireman Uniform",
        "Golf Outfit",
        "Golf Skirt",
        "Halloween Costume Skeleton",
        "Halloween Costume Skull",
        "Halloween Costume Witch",
        "Halloween Costume Witch Hat",
        "Pastor’s Vestments",
        "Pumpkin Grenade",
        "Tattered Mole Head",
        "Tattered Mole Outfit",
        "Whitespring Jumpsuit",
        "Plan: Cultist Blade",
        "Plan: Cultist Dagger",
        "Plan: Meat Hook",
        "Plan: Scarecrows",
        "Plan: Sickle",
    ]
}
#rare costumes
rare_costumes = {
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
    "Plan: Vault-Tec Jack O’Lantern"    ,
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: ",
    "Plan: "
    ]
}

spooky_bag = {
    "probability_sum" : 100,
    "items" : [
        good_rewards,
        rare_plans,
        rare_costumes
        ]
    }

for item in spooky_bag["items"]:
    print('probability', item["probability"])
