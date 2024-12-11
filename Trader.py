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
    def give_intro(self):
        print(f"[bold green]Hello Travellor[/bold green]! My name is [bold purple]{self.name}[/bold purple]. [bold yellow]The Worlds best Tradesman[/bold yellow]. Whatever you want, I'll cater! Whether it be [bold red]strengthening yourself[/bold red], buying a few [bold green]safety precautions[/bold green] or finding some neat [bold purple]quests[/bold purple] Im here for you! If a [bold blue]chat[/bold blue] is all you need, Ill be here too. Pleasure to make your aquaintance")
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
            print("Ah, seeking greater power! Lets see what I can do for you...")
        elif action == "Potions":
            print("Looking for potions, are you? I've got just the thing!")
        elif action == "Quests":
            print("Ah, A thirst for adventure compels you ey? Let me sort you out!")
        elif action == "Talk":
            print("[bold]A chat it is!")
            self.talk_event()
        else:
            print("I see.. Maybe next time!")

    def talk_event(self):
        response = questionary.select(
            "What should we talk about!",
            choices= [
                "",
                "",
                "",
                ""
                ]
        ).ask()

    def quest_giver_event(self):
        pass
trader = Trader("Hanayome")
trader.give_intro()
trader.events()
