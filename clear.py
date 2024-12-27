import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")  
    else:
        os.system("clear")  

thing = {
    "name" : [1, 2, 3],
    "Weee" : [1, 6, 3]
}
key = list(thing.keys())[1]
print(key)

