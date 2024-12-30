#start of with a menu thats simply whether you wish to play or not and also a little tutorial guide => a para on things to know
#Asks for a name 
#get spawned into the lobby
#LOBBY => Trader and maze
# Trader is a simple symbol First time engages an introduction but afterwars just engages events
#Maze => Calls PlayerExplore IF THIS BREAKS GET SPAWNED BACK TO LOBBY => if maze.level > 0 make it so you can choose from level 0 -> current
#Else Just continue the explortion
#Once lvl4 is completed, initiate boss battle 
#if win, have little dialogue and lore and break story and finish => GOOD END
#IF lose, Have a shocking convo with boss, they can talk, beckons you to join => if you do => hidden end else: die (bad end) 
import time
from System import menu, clear_console, message, get_name
import questionary
start = menu()
if start == "starting game":
    clear_console()
    skip = questionary.confirm("Would you like to skip the introduction?").ask()
    if skip:
        print(" How boring...")
    else:
        message("Welcome to the land of Tsubaki. A land befallen by great evil.\n", 0.07)
        time.sleep(0.2)
        message("5 Great entities plague the land with their supreme prowess. All as a result of the emergence of the 5 Great Mysteries of Tsubaki...\n", 0.07)
        message("Many tried to free the land from their rule...", 0.07)
        time.sleep(0.5)
        message("None succeeded\n", 0.1)
        time.sleep(1)
        message("Until, a travellor from a distance land full of adventure, arrived in a small village called 'Salé'. A travellor who would change the fate of Tsubaki forever\n", 0.1)
        message("That travellors name was...\n", 0.2)
    name = get_name()
    message(f"{name}...", 0.2)
    message("It truly was a befitting name.\n", 0.08)
    message(name, 0.1)
    message(", the Hero of Tsubaki...\n", 0.07)
    message("I shall show you their story...\n", 0.08)
    message("A story of ", 0.1)
    message("tragedy ", 0.01)
    message("and", 0.05)
    message(" heroism...\n", 0.07)
    message("Let us begin...", 0.1)
    #go to lobby
