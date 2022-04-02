#!
from traceback import print_tb
import game, time

game.welcome("EN", "Grow the World", "Samuel Orman-Chan")

you = game.player()
baseInv = []
yours = game.inventory(baseInv)

print ("""Hello and welcome to the Solar State.
You are a resident of Sol IV working as a bio-hatchery co-ordinator at the Eastern Equitorial Terraforming Station Hatchery.
You are a Beta+ human, de-bottled 10422AF in Subterrainian Settlement Gamma-V Eastern Hatchery, Sol IV.""")

#print("You have the following metrics as measured by the Solar State Human Assessment and Apparaisal Service.")

input("Press ENTER to continue.")

print("Your task is to help expand the Tropical Agricultural Fascilities whilst the savage reserve is being relocated.\nWorld Controller Kieran Mao requested your personal prescence for this task.")

currentPos = game.checkPoint(0,0)

begin = game.prompt("Accept?", "Yes or No")
if "y" in begin.lower():
    print("Task Accepted.")
    time.sleep(0.5)
    currentPos = game.checkPoint(currentPos, 1)
    print("You have arrived at the T.A.F. Hatchery. East of you is the Hatchery Entrance. West is the Monorail Station you just left.\nNorth is the Feelie Centre and South is your newly assigned residential complex.")

    yours.sysAdd("BioKey for Residential Complex")
    doDirection = game.prompt("What do you want to do?", "Go North, Go South, Go East, Go West or Check your Inventory?")
    if "north" in doDirection.lower():
        currentPos = game.checkPoint(currentPos, 1)
        print("You have entered the Feelie Centre. The scent of soma gas whafts through the air. You start to feel at ease and a little euphoric. Ahead are the booths, to the left is the dance floor, to the right, the auto-songster and the exit is behind.")
        feelieDo = game.prompt("Where do you go?", "Forwards, Backwards, Left or Right.")
        if "forwards" in feelieDo.lower():
            #booths
            print()
        elif "backwards" in feelieDo.lower():
            #Exit
            print()
        elif "left" in feelieDo.lower():
            #dance
            print()
        elif "right" in feelieDo.lower():
            #autoSongster
            print()

else: 
    print ("Task Rejected. Take a soma.")
    time.sleep(5)
    raise SystemExit



