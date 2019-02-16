import math
import random
# debug


debug_weapon = {
    "Name" : "Worldsmasher",
    "VitMod" : 10.0,
    "EndMod" : 20.0,
    "IntMod" : 5.0,
    "MinVit" : 0.0,
    "MinEnd" : 0.0,
    "MinInt" : 0.0,
    "Type"  : "Weapon",
    }
# skill arrays represent stat modify *Vit + *End + *Int + Flat
# possibilities of speicals calling methods
# negative costs for healing
#Type Passive or Active
debug_attack = {
    "Name": "Celestial Swipe",
    "Type": "Acitve",
    "HpCost": ["0","0","0","0"],
    "SpCost": ["0","0","0","0"],
    "MpCost": ["0","0","0","0"],
    "single": ["1","1","1","50"],
    "all": ["0","0","0","50"],

}


# GAMEDATA

# multipliers for the stas of each type - Knight[0], Ranger[1], Mage[2]
types = [[1.5,1.0,1.0],[1.0,1.5,1.0],[1.0,1.0,1.5]]
#these could be beter
enemy_Sprites = [["<","(","x","_","x",")","<"] , ["<","(","O","^","O",")",">"],["<","(","V","_","V",")",">","*"]]\
# these could be better
enemy_Names = ["Abrielle","Adair","Adara","Adriel","Aiyana","Alissa","Alixandra","Altair","Amara","Anatola","Anya","Arcadia","Ariadne","Arianwen","Aurelia","Aurelian","Aurelius","Avalon","Acalia","Alaire","Auristela","Bastian","Breena","Brielle","Briallan","Briseis","Cambria","Cara","Carys","Caspian","Cassia","Cassiel","Cassiopeia","Cassius","Chaniel","Cora","Corbin","Cyprian","Daire","Darius","Destin","Drake","Drystan","Dagen","Devlin","Devlyn","Eira","Eirian","Elysia","Eoin","Evadne","Eliron","Evanth","Fineas","Finian","Fyodor","Gareth","Gavriel","Griffin","Guinevere","Gaerwn","Ginerva","Hadriel","Hannelore","Hermione","Hesperos","Iagan","Ianthe","Ignacia","Ignatius","Iseult","Isolde","Jessalyn","Kara","Kerensa","Korbin","Kyler","Kyra","Katriel","Kyrielle","Leala","Leila","Lilith","Liora","Lucien","Lyra","Leira","Liriene","Liron","Maia","Marius","Mathieu","Mireille","Mireya","Maylea","Meira","Natania","Nerys","Nuriel","Nyssa","Neirin","Nyfain","Oisin","Oralie","Orion","Orpheus","Ozara","Oleisa","Orinthea","Peregrine","Persephone","Perseus","Petronela","Phelan","Pryderi","Pyralia","Pyralis","Qadira","Quintessa","Quinevere","Raisa","Remus","Rhyan","Rhydderch","Riona","Renfrew","Saoirse","Sarai","Sebastian","Seraphim","Seraphina","Sirius","Sorcha","Saira","Sarielle","Serian","Séverin","Tavish","Tearlach","Terra","Thalia","Thaniel","Theia","Torian","Torin","Tressa","Tristana","Uriela","Urien","Ulyssia","Vanora","Vespera","Vasilis","Xanthus","Xara","Xylia","Yadira","Yseult","Yakira","Yeira","Yeriel","Yestin","Zaira","Zephyr","Zora","Zorion","Zaniel","Zarek"]

#BACKEND
def new_enemy(Pos,type,level=1):
    stats = {
    "Name" : Get_EnemyName(),
    "HP" : math.sqrt(level)*1000.0,
    "Damage" : math.sqrt(level)*25.0,
    "Type" : type,
    "Pos" : Pos,
    }
    return stats

def Get_EnemyName():
    n1 = random.choice(enemy_Names)
    n2 = random.choice(enemy_Names)
    while n1 == n2:
        n2 = random.choice(enemy_Names)
    return(n1 + " " + n2)

def level_player(type,level=1):
    stats = {
    "Vitality" : level*types[type][0],
    "Endurance" : level*types[type][1],
    "Intelligence" : level*types[type][2],
    "level" : level,
    "item 1" : "empty",
    "item 2" : "empty",
    "weapon" : {"Name": "none"},
    "armour" : {"Name": "none"},
    "ring" : {"Name": "none"},
    "inv" : [],
    "skills":[],
    }
    stats["MaxHp"] = math.sqrt(stats["Vitality"]) * 1000.0
    stats["MaxSp"] = math.sqrt(stats["Endurance"]) * 1000.0
    stats["MaxMp"] = math.sqrt(stats["Intelligence"]) * 1000.0
    stats["CurrentHp"] = stats["MaxHp"]
    stats["CurrentSp"] = stats["MaxSp"]
    stats["CurrentMp"] = stats["MaxMp"]
    return stats

def new_item(health_gain = 0, stamina_gain = 0, mana_gain = 0, keyLevel = 0):
    output = []
    output.append(health_gain)
    output.append(stamina_gain)
    output.append(mana_gain)
    output.append(keyLevel)
    return output

def Game_Tick():
    for enemy in enemy_list:
        player["CurrentHp"] = player["CurrentHp"] - enemy["Damage"]
        print(enemy["Name"] + ": " + str(enemy["HP"]))
    print("Your HP: " + str(player["CurrentHp"]) + "/" + str(player["MaxHp"]))
    print("Your SP: " + str(player["CurrentSp"]) + "/" + str(player["MaxSp"]))
    print("Your MP: " + str(player["CurrentMp"]) + "/" + str(player["MaxMp"]))
    if player["CurrentHp"] <= 0:
        Lose()
def Lose():
    #calculate score here
    score = 0
    print("You Lost, Final Score: " + str(score))

def show_Inventory(player_id):
    print("Weapon:" + str(player_id["weapon"]))
    print("Armour:" + str(player_id["armour"]))
    print("Ring:" + str(player_id["ring"]))
    print("Carrying:")
    for item in player_id["inv"]:
        print(item)
    q = input("Equip?:")
    if q in player_id["inv"]:
        pass
    else:
        print("unable to equip")
def show_Skills(player_id):
    pass
#MEMORY DATA

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
        if True:
            show_Inventory(player)
            Get_input()
        else:
            print("unable to acess inventory, there are enemies nearby")
    elif command == "skills":
        if True:
            show_Skills(player)
            Get_input()
        else:
            print("unable to check skills, there are enemies nearby")
    elif command == "continue" and True:
        pass
    elif command == "help":
        print("attack 1-3,\nitem 1-2,\ncontinue,\nsave,\ninv or skills")
        Get_input()
    elif command == "attack 1":
        pass
    elif command == "attack 2":
        pass
    elif command == "attack 3":
        pass
    elif command == "item 1":
        pass
    elif command == "item 2":
        pass
    elif command == "save":
        pass
    else:
        print("invalid command")
        Get_input()

#Init
enemy_list = []
enemy_list.append(new_enemy((25,25),0))
enemy_list.append(new_enemy((6,13),0))
enemy_list.append(new_enemy((12,9),1))
enemy_list.append(new_enemy((19,55),2))
player = level_player(1)
player["weapon"] = debug_weapon
print(player)

# Game loop
while True:
    Make_Room(enemy_list)
    Get_input()
    Game_Tick()


#SAVING AND LOADING
