#!
from importlib.resources import contents
import random

def welcome(lang):
    if lang == "EN":
        print("Welcome to TEXT GAME")
        print("Credit: TODO")
    elif lang == "EO":
        print("Bonvenon a Ludo de Teksto")
        print("Faritaj de: TODO")
    elif lang == "FR":
        print("Bienvenue au Jeu de Texte")
        print("Fait par: TODO")
    
def prompt(Question, Options):
    print(Question)
    print("Your Options are:",Options)
    uPrompt = input ("> ")
    return uPrompt

class inventory:
    contents = []
    def __init__(self, contents):
        self.contents = contents

    def check():
        print ("In your inventory, you have:")
        if inventory.contents:
            for i in inventory.contents:
                print(i)
        else: print("Nothing. Sorry about that.")

    def pickup(item):
        inventory.contents.append(item)
        print("You have picked up", item)
    def drop(item):
        if item in inventory.contents:
            inventory.contents.remove(item)
            print(item, "dropped.")
        else: print ("Couldn't drop", item, "as it isn't in your inventory.")

def checkPoint(currPos, distance):
    return int(currPos) + int(distance)

class player:
    def __init__(self):
        self.health = 25
        self.skill = 1
        self.intellect = random.randint(1,5)
    
    def doTask(task):
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

