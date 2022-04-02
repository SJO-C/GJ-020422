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


        