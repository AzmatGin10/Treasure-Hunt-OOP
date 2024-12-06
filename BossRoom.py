#a true and false jagged array, with one string within
#how to convert true to #, False to " " and keep the string
#differentiate from the types
#a function to help with that, takes in cell, and gets and return the desired outcome
#a function to collate it all
#=> perfom convert function on each cell of each row and adds it all together

def ConvertCell(cell):
    if cell == "":
        return "*"
    elif cell: 
        return "#" 
    else:
        return " "
    


def PrintMaze(maze):
    final_maze = []
    for row in maze:
        converted_row = [ConvertCell(cell) for cell in row]
        final_maze.append(converted_row)
    for row in final_maze:
        print("  ".join(x for x in row))

def Movement(maze, location):
    UserInput = input()
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    if UserInput == "w":
        pass
    elif UserInput == "a":
        pass
    elif UserInput =="s":
        pass
    elif UserInput == "d":
        pass
    else:
        pass
             
BossRoom = [
    [True, True, True, True, True, True, True, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, False, False, "", False, False, False, True],
    [True, False, False, False, False, False, False, True],
    [True, True, True, False, False, True, True, True],
]



#while True:
    #input()
    
maze = PrintMaze(BossRoom)
for row in maze:
    print(row)
