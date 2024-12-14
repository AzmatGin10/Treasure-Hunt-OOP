import random
from clear import clear_console
import getch  # Unix





#player, enemy, chests, choose start, choose end position 
#start pos = position of generation
class Maze:
    def __init__(self, player, enemy, mazeSize):
        self.player = player
        self.enemy = enemy
        self.mazeSize = mazeSize
        self.startX = 2*random.randint(0, self.mazeSize//2 - 1) + 1
        self.startY = 2*random.randint(0, self.mazeSize//2 - 1) + 1
        self.maze = self.Generate()
    def Generate(self):
        directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        maze = [[True]*self.mazeSize for x in range(self.mazeSize)]
        
        stack = [(self.startX, self.startY)]
        while len(stack) > 0:
            currentX, currentY = stack[-1]
            if (maze[currentY][currentX]):
                maze[currentY][currentX] = False
            random.shuffle(directions)
            
            neighbours = []
            
            for dir in directions:
                midX, midY = currentX + dir[0], currentY + dir[1]
                newX, newY = midX + dir[0], midY + dir[1]
                
                if 0 <= newX < self.mazeSize and 0 <= newY < self.mazeSize and maze[newY][newX] and maze[midY][midX]:
                    neighbours.append((newX, newY, midX, midY))

            if neighbours:
                newX, newY, midX, midY = random.choice(neighbours)
                maze[newY][newX] = False
                maze[midY][midX] = False
                stack.append((newX, newY))
            else:
                stack.pop()            
        return maze
    def endpos(self):
        pass
    def ConvertCell(self, cell):
        if isinstance(cell, str):
            return cell
        elif cell: 
            return "#" 
        else:
            return "."
    def PrintMaze(self, maze):
        final_maze = []
        for row in maze:
            converted_row = [self.ConvertCell(cell) for cell in row]
            final_maze.append(converted_row)
        for row in final_maze:
            print("  ".join(x for x in row))
    def PlayerExplore(self):
        playerX, playerY = self.startX, self.startY
        def IsValidMove(maze, positionX, positionY):
            print((positionX, positionY))
            return 0 < positionX < self.mazeSize and 0 < positionY < self.mazeSize and not maze[positionY][positionX]
        self.maze[self.startY][self.startX] = "@"
        while True:
            clear_console()
            self.PrintMaze(self.maze)
            PlayerInput = getch.getch()
             
            print((playerX, playerY))
            if PlayerInput == "w":
                if IsValidMove(self.maze, playerX, playerY-1):
                    self.maze[playerY][playerX] = False
                    playerX, playerY = playerX, playerY-1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
            elif PlayerInput == "a":
                if IsValidMove(self.maze, playerX-1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX, playerY = playerX-1, playerY
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "s":
                if IsValidMove(self.maze, playerX, playerY+1):
                    self.maze[playerY][playerX] = False
                    playerX, playerY = playerX, playerY+1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "d":
                if IsValidMove(self.maze, playerX+1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX, playerY = playerX+1, playerY
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)

#start off with directions to travel
#function for movement will work on the base mazethat hasnt been converted, => self, playerpostion, enemy position 
#every input w a s d => clear console and printmaZE again
#1) take in user input of wasd, and check if it is a valid movement => the cell is False and = > 0 <= newX < self.mazeSize and 0 <= newY < self.mazeSize
#convert current cell to False and next cell to player symbol
#reprint the maze, have a while loop to repeat this process

maze = Maze("", "", 21)

maze.PlayerExplore()


