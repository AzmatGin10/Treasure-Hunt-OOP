#a true and false jagged array, with one string within
#how to convert true to #, False to " " and keep the string
#differentiate from the types
#a function to help with that, takes in cell, and gets and return the desired outcome
#a function to collate it all
#=> perfom convert function on each cell of each row and adds it all together

def ConvertCell(cell):
    if isinstance(cell, str):
        return cell
    elif cell: 
        return "#" 
    else:
        return " "
def Valid_move(maze, start, move):
    pass


def PrintMaze(maze):
    final_maze = []
    for row in maze:
        converted_row = [ConvertCell(cell) for cell in row]
        final_maze.append(converted_row)
    for row in final_maze:
        print("  ".join(x for x in row))
         
BossRoom = [
    [True, True, True, True, True, True, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, True, False, "", False, True, True]
]

maze = PrintMaze(BossRoom)

