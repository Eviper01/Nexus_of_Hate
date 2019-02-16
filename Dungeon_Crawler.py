import math
import random

# GAMEDATA

# multipliers for the stas of each type - Knight[0], Ranger[1], Mage[2]
types = [[1.5,1.0,1.0],[1.0,1.5,1.0],[1.0,1.0,1.5]]
enemy_Sprites = [["<","(","x","_","x",")","<"] , ["<","(","O","^","O",")",">"],["<","(","V","_","V",")",">","*"]]


#   <(x_x)<
#
#
#
#BACKEND
def new_enemy(Pos,type,level=1):
    stats = {
    "Name" : 
    "HP" : math.sqrt(level)*1000.0,
    "Damage" : math.sqrt(level)*25.0,
    "Type" : type,
    "Pos" : Pos
    }
    return stats


def level_player(type,level=1):
    stats = {
    "Vitality" : level*types[type][0],
    "Endurance" : level*types[type][1],
    "Intelligence" : level*types[type][2],
    "level" : level,
    "item 1" : "empty",
    "item 2" : "empty",
    "weapon" : "none",
    "armour" : "none",
    "ring" : "none",

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
        print( enemy["HP"])
    print("Your HP: " + str(player["CurrentHp"]) + "/" + str(player["MaxHp"]))
    print("Your SP: " + str(player["CurrentSp"]) + "/" + str(player["MaxSp"]))
    print("Your MP: " + str(player["CurrentMp"]) + "/" + str(player["MaxMp"]))


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
        pass
    elif command == "up":
        pass
    elif command == "down":
        pass
    elif command == "left":
        pass
    elif command == "right":
        pass
    elif command == "help":
        pass
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

enemy_list = []
enemy_list.append(new_enemy((25,25),0))
enemy_list.append(new_enemy((6,13),0))
enemy_list.append(new_enemy((12,9),1))
enemy_list.append(new_enemy((19,55),2))


player = level_player(1)
print(player)

while True:
    Make_Room(enemy_list)
    Get_input()
    Game_Tick()


#SAVING AND LOADING
