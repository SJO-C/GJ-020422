#!
import random

def welcome(lang, name, credits):
    if lang == "EN":
        print("Welcome to", name)
        print("Credit:", credits)
    elif lang == "EO":
        print("Bonvenon a", name)
        print("Faritaj de:", credits)
    elif lang == "FR":
        print("Bienvenue au", name)
        print("Fait par:", credits)
    
def prompt(Question, Options):
    print(Question)
    print("Your Options are:",Options)
    uPrompt = input ("> ")
    return uPrompt

def checkPoint(currPos, distance):
    return int(currPos) + int(distance)

class inventory:
    contents = []
    def __init__(self, contents):
        self.contents = contents

    def check(self):
        print ("In your inventory, you have:")
        if inventory.contents:
            for i in inventory.contents:
                print(i)
        else: print("Nothing. Sorry about that.")

    def sysAdd(self,item):
        inventory.contents.append(item)
        return inventory.contents
    def pickup(self,item):
        inventory.contents.append(item)
        print("You have picked up", item)
        return inventory.contents
    def drop(self,item):
        if item in inventory.contents:
            inventory.contents.remove(item)
            print(item, "dropped.")
            return inventory.contents
        else: 
            print ("Couldn't drop", item, "as it isn't in your inventory.")
            return inventory.contents


class player:
    def __init__(self):
        self.health = 25
        self.skill = 1
        self.intellect = random.randint(1,5)
    
    def stats(self):
        return str("Health\t{}\nSkill\t{}\nIntellect\t{}\n".format(player.self.health, player.self.skill, player.self.intellect))

    def doTask(self,task):
        difficulty = (player.self.skill * player.self.intellect) - task
        success = random.randint(0,100)
        if difficulty > (player.self.intellect - 1):
            if success >= 75:
                player.self.skill += 1
                return True
            else: return False
        else: 
            if success >= 25:
                player.self.skill += 1
                return True
            else: return False
    
    def hurt(self,damage, armour):
        (player.self.health + (0.1* armour)) - damage

    def heal(self,healModifier):
        if (player.self.health + healModifier) > 25:
            player.self.health = 25
        else:
            player.self.health += healModifier
    

    

