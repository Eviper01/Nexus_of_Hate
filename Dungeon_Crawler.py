import math
import random
from ast import literal_eval

# GAMEDATA

#Skills - have name and a method attached to them

def none(a=0,b=0,c=0):
    pass

def Celestial_Slash(player_id):
    fail = True
    while fail == True:
        try:
            enemy = enemy_list[int(input("Target #?"))-1]
            enemy["CurrentHp"] = enemy["CurrentHp"] - (player_id["Weapon"]["VitMod"]*player_id["Vitality"] + player_id["Weapon"]["EndMod"]*player_id["Endurance"] + player_id["Weapon"]["IntMod"]*player_id["Intelligence"] + 50)
            fail = False
        except:
            print("Invalid Target #")
            fail = True
    for enemy in enemy_list:
        enemy["CurrentHp"] = enemy["CurrentHp"] - 50

# Modifiers


# multipliers for the stas of each type - Knight[0], Ranger[1], Mage[2]
types = [[1.5,1.0,1.0],[1.0,1.5,1.0],[1.0,1.0,1.5]]
#these could be beter
enemy_Sprites = [["<","(","x","_","x",")","<"] , ["<","(","O","^","O",")",">"],["<","(","V","_","V",")",">","*"]]\
# these could be better
enemy_Names = ["Abrielle","Adair","Adara","Adriel","Aiyana","Alissa","Alixandra","Altair","Amara","Anatola","Anya","Arcadia","Ariadne","Arianwen","Aurelia","Aurelian","Aurelius","Avalon","Acalia","Alaire","Auristela","Bastian","Breena","Brielle","Briallan","Briseis","Cambria","Cara","Carys","Caspian","Cassia","Cassiel","Cassiopeia","Cassius","Chaniel","Cora","Corbin","Cyprian","Daire","Darius","Destin","Drake","Drystan","Dagen","Devlin","Devlyn","Eira","Eirian","Elysia","Eoin","Evadne","Eliron","Evanth","Fineas","Finian","Fyodor","Gareth","Gavriel","Griffin","Guinevere","Gaerwn","Ginerva","Hadriel","Hannelore","Hermione","Hesperos","Iagan","Ianthe","Ignacia","Ignatius","Iseult","Isolde","Jessalyn","Kara","Kerensa","Korbin","Kyler","Kyra","Katriel","Kyrielle","Leala","Leila","Lilith","Liora","Lucien","Lyra","Leira","Liriene","Liron","Maia","Marius","Mathieu","Mireille","Mireya","Maylea","Meira","Natania","Nerys","Nuriel","Nyssa","Neirin","Nyfain","Oisin","Oralie","Orion","Orpheus","Ozara","Oleisa","Orinthea","Peregrine","Persephone","Perseus","Petronela","Phelan","Pryderi","Pyralia","Pyralis","Qadira","Quintessa","Quinevere","Raisa","Remus","Rhyan","Rhydderch","Riona","Renfrew","Saoirse","Sarai","Sebastian","Seraphim","Seraphina","Sirius","Sorcha","Saira","Sarielle","Serian","Séverin","Tavish","Tearlach","Terra","Thalia","Thaniel","Theia","Torian","Torin","Tressa","Tristana","Uriela","Urien","Ulyssia","Vanora","Vespera","Vasilis","Xanthus","Xara","Xylia","Yadira","Yseult","Yakira","Yeira","Yeriel","Yestin","Zaira","Zephyr","Zora","Zorion","Zaniel","Zarek"]

loot_levels = ["Poor ","Common ","Unique ","Legendary ","Mythical ","Fabled ",]
loot_levels_potions = ["Weak ","Lesser ","Standard ","Concentrated ","Greater ","Supreme ",]


Weapons = [
 {
    "Name" : "Shortsword",
    "VitMod" : 5.0,
    "EndMod" : 5.0,
    "IntMod" : 0.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 0.0,
    "Weight" : "Light",
    "Type"  : "Weapon",
    },
]
Weapon_Modifiers = [none]
Armours = [
{
    "Name" : "Chainmail",
    "DEF" : 10.0,
    "VitGain" : 0.0,
    "EndGain" : 0.0,
    "IntGain" : 0.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 0.0,
    "Weight" : "Heavy",
    "Type"  : "Armour",
},
]
Armour_Modifiers = [none]
Rings = [{"Name": "none"}]
Ring_Modifiers = [none]
Potions = [
{
"Name" : "Healing Potion",
"HpGain" : 10,
"MpGain": 0,
"SpGain": 0,
"Type": "item",
"Subtype": "Potion",
},
{
"Name" : "Stamina Potion",
"HpGain" : 0,
"MpGain": 10,
"SpGain": 0,
"Type": "item",
"Subtype": "Potion",
},
{
"Name" : "Mana Potion",
"HpGain" : 0,
"MpGain": 10,
"SpGain": 0,
"Type": "item",
"Subtype": "Potion",
},
{
"Name" : "Energy Potion",
"HpGain" : 0,
"MpGain": 5,
"SpGain": 5,
"Type": "item",
"Subtype": "Potion",
},
]
#BACKEND

def find(lst, key, value):
    for i, dic in enumerate(lst):
        if dic[key] == value:
            return i
    return -1

def Get_Loot_Level(x):
    chance = random.random()
    level = (math.ceil(math.log(x,4)))
    if chance <= 0.3:
         level = level - 1
    elif chance >= 0.7:
        level = level + 1
    else:
        level = level
    if level <= 0:
        return 1
    else:
        return level


def Points_to_Percent(x):
    return 100-(1000/math.sqrt((2*x)+100))


def Generate_Potion(loot_level):
    item = random.choice(Potions).copy()
    item["HpGain"] = item["HpGain"]*loot_level
    item["SpGain"] = item["SpGain"]*loot_level
    item["MpGain"] = item["MpGain"]*loot_level
    item["Rarity"] = loot_level
    item["Name"] = loot_levels_potions[loot_level-1] + item["Name"]
    item["id"] = random.random()
    return item

def Generate_Weapon(loot_level):
    item = random.choice(Weapons).copy()
    Modifier = none
    if random.random() < 0.2:
        Modifier = random.choice(Weapon_Modifiers)
    item["VitMod"]  = item["VitMod"]*(loot_level)
    item["EndMod"]  = item["EndMod"]*(loot_level)
    item["IntMod"]  = item["IntMod"]*(loot_level)
    item["MinVit"]  = item["MinVit"]*(loot_level)
    item["MinEnd"]  = item["MinEnd"]*(loot_level)
    item["MinInt"]  = item["MinInt"]*(loot_level)
    item["Rarity"] = loot_level
    item["Modifier"] = Modifier
    item["Name"] = loot_levels[loot_level-1] + item["Name"]
    return item

def Generate_Armour(loot_level):
    item = random.choice(Armours).copy()
    Modifier = none
    if random.random() < 0.2:
        Modifier = random.choice(Armour_Modifiers)
    item["DEF"] = item["DEF"]*(loot_level)
    item["MinVit"]  = item["MinVit"]*(loot_level)
    item["MinEnd"]  = item["MinEnd"]*(loot_level)
    item["MinInt"]  = item["MinInt"]*(loot_level)
    item["VitGain"]  = item["VitGain"]*(loot_level)
    item["EndGain"]  = item["EndGain"]*(loot_level)
    item["IntGain"]  = item["IntGain"]*(loot_level)
    item["Rarity"] = loot_level
    item["Modifier"] = Modifier
    item["Name"] = loot_levels[loot_level-1] + item["Name"]
    return item

def Generate_Ring():
    item = random.choice(Rings).copy()
    Modifier = none
    if random.random() < 0.2:
        Modifier = random.choice(Ring_Modifiers)
    item["Modifier"] = Modifier
    return item


def Generate_Room():
    global Combat
    for i in range(math.ceil(math.log(player["level"]/math.log(4)+random.randint(1,2)))):
        Pos = (random.randint(3,27),random.randint(5,90))
        enemy_list.append(new_enemy(Pos,random.randint(0,2),random.randint((math.ceil(player["level"]-math.sqrt(player["level"]-1))),math.ceil(player["level"]+math.sqrt(player["level"])))))
    Combat = True

def new_enemy(Pos,type,level=1):
    stats = {
    "Name" : Get_EnemyName(),
    "CurrentHp" : math.sqrt(level)*random.randint(800,1200),
    "Damage" : math.sqrt(level)*random.randint(20,30),
    "Type" : type,
    "Pos" : Pos,
    "Level": level,
    }
    return stats

def Get_EnemyName():
    n1 = random.choice(enemy_Names)
    n2 = random.choice(enemy_Names)
    while n1 == n2:
        n2 = random.choice(enemy_Names)
    return(n1 + " " + n2)


def new_player(type,level=1):
    stats = {
    "Class": type,
    "Vitality" : level*types[type][0],
    "Endurance" : level*types[type][1],
    "Intelligence" : level*types[type][2],
    "level" : level,
    "item 1" : {"Name": "none", "Subtype": "none"},
    "item 2" : {"Name": "none", "Subtype": "none"},
    "Attack 1": {"Name":"none", "Method":none},
    "Attack 2": {"Name":"none", "Method":none},
    "Attack 3": {"Name":"none", "Method":none},
    "Weapon" : {"Name": "none"},
    "Armour" : {"Name": "none"},
    "Ring" : {"Name": "none"},
    "inv" : [],
    "skills":[],
    "XP": 0,
    "SX":0,
    }
    stats["MaxHp"] = math.sqrt(stats["Vitality"]) * 1000.0
    stats["MaxSp"] = math.sqrt(stats["Endurance"]) * 1000.0
    stats["MaxMp"] = math.sqrt(stats["Intelligence"]) * 1000.0
    stats["CurrentHp"] = stats["MaxHp"]
    stats["CurrentSp"] = stats["MaxSp"]
    stats["CurrentMp"] = stats["MaxMp"]
    return stats



def level_player(player_id):
    print("level up!")
    player_id["level"] = player_id["level"] + 1
    player_id["Vitality"] = player_id["level"]*types[player_id["Class"]][0]
    player_id["Endurance"] = player_id["level"]*types[player_id["Class"]][1]
    player_id["Intelligence"] = player_id["level"]*types[player_id["Class"]][2]
    player_id["MaxHp"] = math.sqrt(player_id["Vitality"]) * 1000.0
    player_id["MaxSp"] = math.sqrt(player_id["Endurance"]) * 1000.0
    player_id["MaxMp"] = math.sqrt(player_id["Intelligence"]) * 1000.0
    player_id["CurrentHp"] = player_id["MaxHp"]
    player_id["CurrentSp"] = player_id["MaxSp"]
    player_id["CurrentMp"] = player_id["MaxMp"]
    player_id["SX"] = player_id["SX"] + 1




def Damage(attacker,target):
    if target["Armour"] == {"Name": "none"}:
        target["CurrentHp"] = target["CurrentHp"] - attacker["Damage"]
    else:
        if target["Armour"]["Weight"] == "Heavy":
            target["CurrentHp"] = target["CurrentHp"] - (attacker["Damage"]*(100-Points_to_Percent(target["Armour"]["DEF"]))/100)
        if target["Armour"]["Weight"] == "Light":
            chance = random.random()
            if chance <= target["Armour"]["DEF"]:
                pass
            else:
                target["CurrentHp"] = target["CurrentHp"] - attacker["Damage"]

def Game_Tick():
    for enemy in enemy_list:
        if enemy["CurrentHp"] <= 0:
            enemy_list.remove(enemy)
    for enemy in enemy_list:
        Damage(enemy,player)
        print(enemy["Name"] + ": " + str(enemy["CurrentHp"]))
    print("Your HP: " + str(player["CurrentHp"]) + "/" + str(player["MaxHp"]))
    print("Your SP: " + str(player["CurrentSp"]) + "/" + str(player["MaxSp"]))
    print("Your MP: " + str(player["CurrentMp"]) + "/" + str(player["MaxMp"]))
    if player["CurrentHp"] <= 0:
        Lose()
    if len(enemy_list) == 0:
        Room_Cleared()

def Room_Cleared():
    global Combat
    player["XP"] = player["XP"] + 1
    Combat = False
    if player["XP"] >= math.sqrt(player["level"]):
        level_player(player)
    player["CurrentHp"] = player["MaxHp"]
    player["CurrentSp"] = player["MaxSp"]
    player["CurrentMp"] = player["MaxMp"]
    # Grant an item
    print("Room Cleared! ,Check inv for new items")
    chance = random.random()
    if chance <= 0.8:
        player["inv"].append(Generate_Potion(Get_Loot_Level(player["level"])))
    else:
        if chance <= 0.5:
            player["inv"].append(Generate_Ring())
        elif chance <= 0.8:
            player["inv"].append(Generate_Armour(Get_Loot_Level(player["level"])))
        else:
            player["inv"].append(Generate_Weapon(Get_Loot_Level(player["level"])))





def Lose():
    #calculate score here
    score = 0
    print("You Lost, Final Score: " + str(score))
    global Lost
    Lost = True

def show_Inventory(player_id):
    player_id["inv"] = [i for n, i in enumerate(player_id["inv"]) if i not in player_id["inv"][n + 1:]]
    print("Weapon:" + str(player_id["Weapon"]))
    print("Armour:" + str(player_id["Armour"]))
    print("Ring:" + str(player_id["Ring"]))
    print("Item 1:" + str(player_id["item 1"]))
    print("Item 2:" + str(player_id["item 2"]))
    print("Carrying:")
    for item in player_id["inv"]:
        print(item)
    q = input("Equip?:")
    if any(d['Name'] == q for d in player_id["inv"]):
        item =  player_id["inv"][find(player_id["inv"],"Name",q)]
        if item["Type"] == "item":
            slot = input("Which Slot?")
            if slot == "1":
                temp = player_id["item 1"].copy()
                player_id["item 1"] = item.copy()
                player_id["inv"][find(player_id["inv"],"Name",q)] = temp
            elif slot =="2":
                temp = player_id["item 2"].copy()
                player_id["item 2"] = item.copy()
                player_id["inv"][find(player_id["inv"],"Name",q)] = temp
            else:
                print("unable to equip")
        else:
            temp = player_id[item["Type"]].copy()
            player_id[item["Type"]] = item.copy()
            player_id["inv"][find(player_id["inv"],"Name",q)] = temp
    else:
        print("unable to equip")

def Use_Potion(slot,player_id):
    player_id["CurrentHp"] = player_id["CurrentHp"]+(player_id["MaxHp"]*player_id[slot]["HpGain"]/100)
    player_id["CurrentSp"] = player_id["CurrentSp"]+(player_id["MaxSp"]*player_id[slot]["MpGain"]/100)
    player_id["CurrentMp"] = player_id["CurrentMp"]+(player_id["MaxMp"]*player_id[slot]["SpGain"]/100)
    if player_id["CurrentHp"] > player_id["MaxHp"]:
        player_id["CurrentHp"] = player_id["MaxHp"]
    if player_id["CurrentSp"] > player_id["MaxSp"]:
        player_id["CurrentSp"] = player_id["MaxSp"]
    if player_id["CurrentMp"] > player_id["MaxMp"]:
        player_id["CurrentMp"] = player_id["MaxMp"]
    player_id[slot] = {"Name": "none", "Subtype": "none"}

def show_Skills(player_id):
    player_id["skills"] = [i for n, i in enumerate(player_id["skills"]) if i not in player_id["skills"][n + 1:]]
    print("Attack 1:" + str(player_id["Attack 1"]))
    print("Attack 2:" + str(player_id["Attack 2"]))
    print("Attack 3:" + str(player_id["Attack 3"]))
    for skill in player_id["skills"]:
        print(skill)
    q = input("Equip?:")
    if any(d['Name'] == q for d in player_id["skills"]):
        s = input("Which Slot?:")
        if s == "1":
            item = player_id["skills"][find(player_id["skills"],"Name",q)]
            temp = player_id["Attack 1"].copy()
            player_id["Attack 1"] = item.copy()
            player_id["skills"][find(player_id["skills"],"Name",q)] = temp

        elif s == "2":
            item = player_id["skills"][find(player_id["skills"],"Name",q)]
            temp = player_id["Attack 2"].copy()
            player_id["Attack 2"] = item.copy()
            player_id["skills"][find(player_id["skills"],"Name",q)] = temp

        elif s == "3":
            item = player_id["skills"][find(player_id["skills"],"Name",q)]
            temp = player_id["Attack 2"].copy()
            player_id["Attack 2"] = item.copy()
            player_id["skills"][find(player_id["skills"],"Name",q)] = temp
        else:
            print("unable to equip")

    else:
        print("unable to equip")


#FRONTEND



def Draw_room(room,l,h):
    for i in range(h):
        render = None
        render = "".join(room[i])
        print(render)


def Make_Room(enemies, l=100, h=30):
    room = [[" "] * l]
    add = room[0].copy()
    for i in range(h-1):
        room.append(add.copy())
    for i in range(h-1):
        room[i][0] = "#"
        room[i][l-1] = "#"
    for i in range(l):
        room[0][i] = "#"
        room[h-1][i] = "#"
    for i in range(len(enemies)):
        for j in range(len(enemy_Sprites[enemies[i]["Type"]])):
            room[enemies[i]["Pos"][0]][enemies[i]["Pos"][1]+ j] = enemy_Sprites[enemies[i]["Type"]][j]

    Draw_room(room,l,h)
    return room

def Get_input():
    command = input(">")
    if command == "inv":
        if Combat == False:
            show_Inventory(player)
            Get_input()
        else:
            print("unable to acess inventory, there are enemies nearby")
            Get_input()

    elif command == "skills":
        if Combat == False:
            show_Skills(player)
            Get_input()
        else:
            print("unable to check skills, there are enemies nearby")
            Get_input()
    elif command == "continue":
        if Combat == False:
            Generate_Room()
        else:
            print("clear this room before continuing")
            Get_input()
    elif command == "help":
        print("attack 1-3,\nitem 1-2,\ncontinue,\nsave,\ninv or skills")
        Get_input()
    elif command == "attack 1":
        if Combat == True:
            player["Attack 1"]["Method"](player)
        else:
            print("there are no enemies nearby")
            Get_input()
    elif command == "attack 2":
        if Combat == True:
            player["Attack 2"]["Method"](player)
        else:
            print("there are no enemies nearby")
            Get_input()
    elif command == "attack 3":
        if Combat == True:
            player["Attack 3"]["Method"](player)
        else:
            print("there are no enemies nearby")
            Get_input()
    elif command == "item 1":
        if Combat == True:
            if player["item 1"]["Subtype"] == "Potion":
                Use_Potion("item 1",player)
        else:
            print("there are no enemies nearby")
            Get_input()
    elif command == "item 2":
        if Combat == True:
            if player["item 2"]["Subtype"] == "Potion":
                Use_Potion("item 2",player)
        else:
            print("there are no enemies nearby")
            Get_input()
    elif command == "save":
        save()
        Get_input()
    elif command == "load":
        load()
        Get_input()
    elif command == "stats":
        print(player)
        print(enemy_list)
        Get_input()
    else:
        print("invalid command")
        Get_input()
#saving/loading

def save():
    file = open("saves.txt","w")
    file.write(str(player))
    file.close()

def Fix_Data(data):
    while data.find("<") != -1:
        index = data.find("<")
        index_end = data.find(">")
        startFI = data.find(" ",index)
        endFI = data.find(" ", startFI + 1)
        function = data[startFI:endFI]
        data = data[:index] + function + data[index_end+1:]
    return data

def load():
    file = open("saves.txt","r")
    global player
    data = file.read()
    data = Fix_Data(data)
    player = eval(data)


# debug


debug_weapon0 = {
    "Name" : "Worldsmasher",
    "Rarity": 5,
    "Modifier": none,
    "VitMod" : 10.0,
    "EndMod" : 20.0,
    "IntMod" : 5.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 0.0,
    "Weight" : "Heavy",
    "Type"  : "Weapon",
    }
debug_weapon1 = {
    "Name" : "Solar Staff",
    "Rarity": 5,
    "Modifier": none,
    "VitMod" : 0.0,
    "EndMod" : 0.0,
    "IntMod" : 75.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 400.0,
    "Weight" : "Light",
    "Type"  : "Weapon",
    }
debug_weapon2 = {
    "Name" : "debug",
    "Rarity": 5,
    "Modifier": none,
    "VitMod" : 0.0,
    "EndMod" : 100000000.0,
    "IntMod" : 0.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 400.0,
    "Weight" : "Light",
    "Type"  : "Weapon",
    }
debug_attack0 = {
    "Name": "Celestial Slash",
    "Type": "Active",
    "Method": Celestial_Slash,
}

#Init
enemy_list = []
player = new_player(1,1)
Lost = False
Combat = False

player["Weapon"] = Generate_Weapon(Get_Loot_Level(player["level"]))
player["Armour"] = Generate_Armour(Get_Loot_Level(player["level"]))
player["Ring"] = Generate_Ring()
# debug init
player["inv"].append(debug_weapon0)
player["inv"].append(debug_weapon1)
player["inv"].append(debug_weapon2)
player["skills"].append(debug_attack0)



# Game loop
while Lost == False:
    Make_Room(enemy_list)
    Get_input()
    Game_Tick()


#SAVING AND LOADING
