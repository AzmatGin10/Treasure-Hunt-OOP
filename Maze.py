import random
from clear import clear_console
import getch 
from collections import deque 


#adding random enemies to the maze
#number of enemies will be dependent of the maze sieze
#function will only return a set of co ordinates so it wont be displayed on map
#itll be like a pokemon style combat system
#enemies can be anyone aslong as its in path and it is not the start position
#1) filterout the possible posiition of the enemy => check if is False
#2) remove the player position => simple
#3) pick a random number of random coordinates based on mazesize => ask people
#4) store values in initializer => have a array for enemy positions
#5) make it so if the player lands on these position a combat system will be engaged
#6) need a smooth transition back into the map

#chest generation plan
# probability works, just need to hand out all the locations
# number of chests will be the no of possible locations // 2
# in those, dish out the probabilities of chest types 
# itll be a tuple of position and chest type
# 1) write a function for number of chests, getting the tupled position and chests type too in one go
# in main explor function, fimple for loop which changed all position to C, S or G based on if , 1 or 2
# 


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
        self.min_distance = self.mazeSize//2
        self.exitX = None
        self.exitY = None
        self.chestweights = [
            #C   S   G
            [90, 10, 0],  #0
            [70, 30, 0],  #1
            [60, 30, 10], #2
            [50, 35, 15], #3
            [30, 50, 20]  #4
        ]

        self.level = 0
        self.enclosed_areas = None

    def CleanUp(self):
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
    
    def BossRoom(self):
        BossRoom = [
    [True, True, True, True, True, True, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, False, False, False, False, False, True],
    [True, True, False, "@", False, True, True]
]
        return BossRoom
    def EndPos(self):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        bfs_queue = deque([(self.startX, self.startY)])
        distanceLevels = {(self.startX, self.startY): 0}
        current_distance = 0
        result = []
        max_retries = 10
        retries = 0
        while bfs_queue:
            nextLevel = []

            for i in range(len(bfs_queue)):
                currentX, currentY = bfs_queue.popleft()

                if current_distance > self.min_distance:
                    result.append((currentX, currentY))

                random.shuffle(directions)

                for dir in directions:

                    newX, newY = currentX + dir[0], currentY + dir[1]

                    if 0 < newX < self.mazeSize and 0 < newY < self.mazeSize and not self.maze[newY][newX] and (newX, newY) not in distanceLevels:
                        distanceLevels[(newX, newY)] = current_distance + 1
                        nextLevel.append((newX, newY))

            bfs_queue.extend(nextLevel)
            current_distance += 1 

        exits = []
        for cell in result:
            wall_count = 0
            for dir in directions:
                neighbourX, neighbourY = cell[0] + dir[0], cell[1] + dir[1]

                if 0 <= neighbourX < self.mazeSize and 0 <= neighbourY < self.mazeSize and self.maze[neighbourY][neighbourX]:
                    wall_count += 1

            if wall_count == 3:
                exits.append(cell)
        while len(exits) <= 1 and retries < max_retries:
            self.CleanUp()  
            retries += 1
            return self.EndPos()

        exit = random.choice(exits)
        exits.remove(exit)
        self.exitX, self.exitY = exit[0], exit[1]
        self.enclosed_areas = exits

    def ConvertCell(self, cell):
        if isinstance(cell, str):
            return cell
        elif cell: 
            return "□" 
        else:
            return " "
        
    def PrintMaze(self, maze):
        final_maze = []
        for row in maze:
            converted_row = [self.ConvertCell(cell) for cell in row]
            final_maze.append(converted_row)
        for row in final_maze:
            print("  ".join(x for x in row))
    def SpawnEnemy(self):
        maze = self.maze
        no_of_enemies = self.mazeSize//5
        enemy_locations = []
        
        for cell in maze:
            enemyX, enemyY = random.randint(1, self.mazeSize-1), random.randint(1, self.mazeSize-1)
            if not maze[enemyY][enemyX] and enemyX != self.startX and enemyY != self.startY:
                enemy_locations.append((enemyX, enemyY))
                enemyX, enemyY = random.randint(1, self.mazeSize-1), random.randint(1, self.mazeSize-1)
            if len(enemy_locations) == no_of_enemies:
                break
        return enemy_locations
    
    def WeightedChance(self):
        weights = self.chestweights[self.level] 
        weight_total = 100 - random.randint(0, 100)
        i = len(weights) - 1
        for x in weights:
            if weight_total <= weights[i]:
                return i
            else:
                weight_total -= weights[i]
                i -= 1

    def Chests(self):
        result = []
        no_of_chests = round(len(self.enclosed_areas)/2)
        for x in self.enclosed_areas:
            result.append(((x), self.WeightedChance()))
            if len(result) == no_of_chests:
                break
        return result    
    def PlayerExplore(self):
        #set up maze and generate needed assets
        enemies = self.SpawnEnemy()
        self.EndPos()
        chests = self.Chests()
        chest_positions = [x[0] for x in chests]
        playerX, playerY = self.startX, self.startY
        
        #validation 
        def IsValidMove(maze, positionX, positionY):
            if positionX == self.exitX and positionY == self.exitY and not have_key:
                return False
            return 0 < positionX < self.mazeSize and 0 < positionY < self.mazeSize and not maze[positionY][positionX] or isinstance(maze[positionY][positionX], str)
        
        #initialise all entities
        have_key = False
        self.maze[self.startY][self.startX] = "◈"
        self.maze[self.exitY][self.exitX] = "E"
        for x in chests:
            chestX, chestY = x[0][0], x[0][1]
            self.maze[chestY][chestX] = "T"
        key =  random.choice(chest_positions)
        input("Note: '◈' is the player\n'E' is the exit\nenemies are random and invisible\n'T' is Treasure")
        
        #maze exploration while loop
        while True:
            clear_console()
            
            self.PrintMaze(self.maze)
            PlayerInput = getch.getch()
            for enemy in enemies:
                if playerX == enemy[0] and playerY == enemy[1]:
                    clear_console()
                    input("You encountered an enemy!\nGet ready for Combat!")
                    enemies.remove((playerX, playerY))
                    #initialise combat
            if PlayerInput == "w":
                if IsValidMove(self.maze, playerX, playerY-1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY-1
                    self.maze[playerY][playerX] = "◈"
                    clear_console()
                    self.PrintMaze(self.maze)
            elif PlayerInput == "a":
                if IsValidMove(self.maze, playerX-1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX = playerX-1
                    self.maze[playerY][playerX] = "◈"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "s":
                if IsValidMove(self.maze, playerX, playerY+1):
                    self.maze[playerY][playerX] = False
                    playerY = playerY+1
                    self.maze[playerY][playerX] = "◈"
                    clear_console()
                    self.PrintMaze(self.maze)
                
            elif PlayerInput == "d":
                if IsValidMove(self.maze, playerX+1, playerY):
                    self.maze[playerY][playerX] = False
                    playerX= playerX+1
                    self.maze[playerY][playerX] = "◈"
                    clear_console()
                    self.PrintMaze(self.maze)
            if (playerX, playerY) == (self.exitX, self.exitY):
                print("Well done! You have completed the maze!")
                break
            if (playerX, playerY) in chest_positions:
                
                input("You found a Chest! You opened it and found...")
                if (playerX, playerY) == key:
                    input("A key!⚿ You can now Leave!")
                    have_key = True
                else:
                    input("Nothing...")

            
maze = Maze("", "", 13)
maze.PlayerExplore()








 
