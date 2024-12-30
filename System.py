import questionary
import os
import platform
from art import text2art
import time
import sys
import getch
def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  
def message(sentence, delay):
    for char in sentence:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
def get_name():
    response = questionary.text("What's your name?").ask()
    confirm = questionary.confirm(f"{response}... Is this correct?").ask()
    if confirm:
        return response
    else:
        return get_name()
def game_over():
    Art = text2art("GAME OVER!")
    print(Art)
def menu():
    clear_console()
    Art = text2art("WELOCOME TO\n             TSUBAKI")
    print(Art)
    response = questionary.select(
        "What would you like to do",
        choices=[
            "Start Game!",
            "Tutorial!",
            "Leave..."
        ]
    
    ).ask()
    if response == "Start Game!":
        return "starting game"
    if response == "Tutorial!":
        message("The main purpose of the game is to complete all levels of the maze and kill the boss, ending the game. To access your loadout, press 'i' in the lobby\nYou will be reminded of this in the maze so do not worry\nAnything else is self explanatory so I will leave you be\nHave fun!", 0.03)
        print("\npress any key to continue...")
        Input = getch.getch()
        
        if Input:

            return menu()
    if response == "Leave...":
        print("Leaving...")
        time.sleep(3)
def lobby():
    pass
