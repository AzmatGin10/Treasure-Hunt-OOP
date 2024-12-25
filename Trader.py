
#Buy weapons, armour and health potions => TradeEvent()
#A place to talk and get infomation => TalkEvent()
#A place to get side quests, simpke things like getting a certain weapon QuestGiverEvent()
#attributes => none
#methods => GiveIntro() TradeEvent() TalkEvent() QuestGiverEvent()
import questionary
from rich import print
from clear import clear_console
clear_console()
class Trader():
    def __init__(self, name):
        self.name = name
        self.quests = []
    def give_intro(self):
        print(f"[bold green]Hello Travellor[/bold green]! My name is [bold blue]{self.name}[/bold blue]. [bold yellow]The Worlds best Tradesman[/bold yellow]. Whatever you want, I'll cater! Whether it be [bold red]strengthening yourself[/bold red], buying a few [bold green]safety precautions[/bold green] or finding some neat [bold purple]quests[/bold purple] Im here for you! If a [bold blue]chat[/bold blue] is all you need, Ill be here too. Pleasure to make your aquaintance")
    def events(self):
        action = questionary.select(
            "What would you like to do?",
            choices= [
            "Strengthen self",
            "Potions",
            "Quests",
            "Talk", 
            "Maybe later..."
            ]
        ).ask()
        if action == "Strengthen self":
            clear_console()
            print("Ah, seeking greater power! Lets see what I can do for you...")
            self.buy_arms("Place holder")
        elif action == "Potions":
            clear_console()
            print("Looking for potions, are you? I've got just the thing!")
            #self.potions()
        elif action == "Quests":
            clear_console()
            print("Ah, A thirst for adventure compels you ey? Let me sort you out!")
            self.quest_giver_event()
        elif action == "Talk":
            clear_console()
            print("[bold]A chat it is!")
            self.talk_event()
        else:
            clear_console()
            print("I see.. Maybe next time!")

    def talk_event(self):
        response = questionary.select(
            "What should we talk about!",
            choices= [
                "What is this place?",
                "What are Raiju?",
                "Why do people keep going into mazes?",
                "How do we get rid of the Raiju?",
                "Hello!",
                "Back"
                ]
        ).ask()
        if response == "What is this place?":
            print("We are a humble village in the outskirts of [bold purple]Tsubaki[/bold purple]. While we may not be as extravagent or powerful as other villages , our strong sense of [bold yellow]community[/bold yellow] helps us thrive. We make a living off of passing trade with travellors such as [bold green]you[/bold green]. Its peaceful...Though, things has started to change recently... we fear for the worst since the arrival of the [bold red]Raiju.")
            input()
            clear_console()
            return self.talk_event()
        elif response == "What are Raiju?":
            print("[bold red]The Raiju[/bold red]... They're not like us. One day, a new world addition to the [bold]five great mysteries of Tsubaki[/bold] appeared abruptly. A maze. Grand yet desolate. Its achitecture truly unparalleled. A true wonder. It was met with curiosity at first. We were not sure of what to think. However, after the [bold red]Mayor[/bold red] went inside... We don't speak of what happened. Its all their fault. The [bold]Raiju. They dont belong in our realm.")
            input()
            clear_console()
            return self.talk_event()
        elif response == "Why do people keep going into mazes?":
            print("To change our reality. No matter how overwhelming the task, humans like us, we [bold yellow]struggle[/bold yellow], we [bold yellow]fight[/bold yellow] and [bold yellow]never yield[/bold yellow]. All in hopes of carving a beautiful future for the next generation, entrusting the same task to them... Too much?")
            input()
            clear_console()
            return self.talk_event()
        elif response == "How do we get rid of the Raiju?":
            print("We dont know. We've sent countless recon groups into the maze, none of them have made it back. However, a great being is sensed at the end of the maze, we assume if [bold red]'He'[/bold red] is slayed, all will revert back to how it was, how it should be.")
            input()
            clear_console()
            return self.talk_event()
        elif response == "Hello!":
            print("[bold purple] Hi?...... I know i said I'd chat with you but, this really isnt what i had in mind")
            input()
            clear_console()
            return self.talk_event()
        else:
            clear_console()
            return self.events()

    def quest_giver_event(self):
        print("Here are the currently availabe quests.")
    def buy_arms(self, player):
        response = questionary.select(
            "Have a look!",
            choices = [
            "Weaponry",
            "Armour",
            "Back"
            ]



        ).ask()
        if response == "Weaponry":
            pass
        elif response == "Armour":
            pass
        else:
            return self.events()

#trader = Trader("Hanayome")
#trader.give_intro()
#trader.events()


