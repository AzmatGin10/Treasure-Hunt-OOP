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
        self.min_distance = self.mazeSize
        self.exitX = None
        self.exitY = None
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
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited =set()
        bfs_queue = [((self.startX, self.startY), 0)]
        result = []
        filtered_result = []
        visited.add((self.startX, self.startY))
        while bfs_queue:
            (current_x, current_y), current_distance = bfs_queue.pop(0)

            if current_distance > self.min_distance:
                result.append((current_x, current_y))

            random.shuffle(directions)

            
            for dir in directions:

                new_x, new_y = current_x + dir[0], current_y + dir[1]

                if 0 < new_x < self.mazeSize and 0 < new_y < self.mazeSize and not self.maze[new_y][new_x]:

                    if (new_x, new_y) not in visited:
                        visited.add((new_x, new_y))
                        bfs_queue.append(((new_x, new_y), current_distance+1))
        for cell in result:
            count = 0
            
            for dir in directions:
                neighbour = (cell[0] + dir[0], cell[1] + dir[1])
                
                if self.maze[neighbour[0]][neighbour[1]]:
                    count += 1
            if count == 3:
                filtered_result.append(cell)
                count = 0
            
        exit = filtered_result[random.randint(0, len(filtered_result)-1)]
        self.exitX = exit[1]
        self.exitY = exit[0]

    def ConvertCell(self, cell):
        if isinstance(cell, str):
            return cell
        elif cell: 
            return "#" 
        else:
            return " "
    def PrintMaze(self, maze):
        final_maze = []
        for row in maze:
            converted_row = [self.ConvertCell(cell) for cell in row]
            final_maze.append(converted_row)
        for row in final_maze:
            print("  ".join(x for x in row))
    def PlayerExplore(self):
        self.endpos()
        playerX, playerY = self.startX, self.startY
        def IsValidMove(maze, positionX, positionY):
            print((positionX, positionY))
            return 0 < positionX < self.mazeSize and 0 < positionY < self.mazeSize and not maze[positionY][positionX] or isinstance(maze[positionY][positionX], str)
        self.maze[self.startY][self.startX] = "@"
        self.maze[self.exitY][self.exitX] = "E"
        while True:
            clear_console()
            self.PrintMaze(self.maze)
            PlayerInput = getch.getch()
             
            if PlayerInput == "w":
                if IsValidMove(self.maze, playerX, playerY-1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY-1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
            elif PlayerInput == "a":
                if IsValidMove(self.maze, playerX-1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX = playerX-1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "s":
                if IsValidMove(self.maze, playerX, playerY+1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY+1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "d":
                if IsValidMove(self.maze, playerX+1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX= playerX+1
                    self.maze[playerY][playerX] = "@"
                    clear_console()
                    self.PrintMaze(self.maze)
            if (playerX, playerY) == (self.exitX, self.exitY):
                print("Well done! You have completed the maze!")
                break
maze = Maze("", "", 21)
maze.PlayerExplore()


#adding an exit to the maze
#use bfs to find a nod with a certain distance away from the start postition
#its neighbours must all be True except for 1 => means it is an enclosed area
#distacnce will be determined based on mazesize for generalisation
#change cell into a string for exit some symbol => "E"
#1 use bfs to find possible nodes that could be an exit, reaches a threshold of distance
#2 filters out the nodes based on thier nieghbours to see if it has the above requiremnet
#3 have a list of possible exits and choose a random one of the list


