import random
#move and render screen when they do valid movement
#False [][] 
#store position in player
#access curent state
#statemachine
#each class is derived from base state => will be maze state 
#player, enemy, chests, choose start, choose end position 
#start pos = position of generation
class Maze:
    def __init__(self, player, enemy, mazeSize):
        self.player = player
        self.enemy = enemy
        self.mazeSize = mazeSize
        self.startX = 2*random.randint(0, self.mazeSize//2 - 1) + 1
        self.startY = 2*random.randint(0, self.mazeSize//2 - 1) + 1
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
            return " "
    def PrintMaze(self, maze):
        final_maze = []
        for row in maze:
            converted_row = [self.ConvertCell(cell) for cell in row]
            final_maze.append(converted_row)
        for row in final_maze:
            print("  ".join(x for x in row))




maze = Maze("", "", 9)
maze.PrintMaze(maze.Generate())

