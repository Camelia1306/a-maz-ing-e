
class Cat:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy, maze):
        """Muta pisica doar daca noua pozitie este libera"""
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < len(maze[0]) and 0 <= new_y < len(maze) and maze[new_y][new_x] == 0:
            self.x = new_x
            self.y = new_y
