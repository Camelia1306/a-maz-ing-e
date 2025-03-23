import pygame

# Dimensiuni
SCREEN_SIZE = 600
GRID_SIZE = 3  #TODO: modifica  dinamic la 2, 3, 4, etc.
CELL_SIZE = SCREEN_SIZE // (GRID_SIZE * GRID_SIZE)
MAZE_SIZE = GRID_SIZE * GRID_SIZE  # Dimensiunea totala a labirintului

# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def draw_maze(screen, maze, visible_zones):
    """Deseneaza doar zonele vizibile ale labirintului"""
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            grid_x, grid_y = x // (MAZE_SIZE // GRID_SIZE), y // (MAZE_SIZE // GRID_SIZE)
            if (grid_x, grid_y) in visible_zones:
                color = WHITE if maze[y][x] == 0 else BLACK
            else:
                color = BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_goal(screen):
    """Deseneaza punctul de final in coltul stanga sus"""
    pygame.draw.rect(screen, GREEN, (0, 0, CELL_SIZE, CELL_SIZE))

def draw_cat(screen, cat):
    """Deseneaza pisica in labirint"""
    pygame.draw.circle(screen, BLUE, (cat.x * CELL_SIZE + CELL_SIZE // 2, cat.y * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 3)

def update_visible_zones(cat, visible_zones):
    """Adauga mini-labirintul curent la zonele vizibile"""
    grid_x = cat.x // (MAZE_SIZE // GRID_SIZE)
    grid_y = cat.y // (MAZE_SIZE // GRID_SIZE)

    # Adauga zona curenta
    visible_zones.add((grid_x, grid_y))
    #
    #  # Verifica si arata zonele de langa
    # if cat.x % (MAZE_SIZE // GRID_SIZE) == 0:
    #     visible_zones.add((grid_x - 1, grid_y))
    # if cat.y % (MAZE_SIZE // GRID_SIZE) == 0:
    #     visible_zones.add((grid_x, grid_y - 1))
    # if cat.x % (MAZE_SIZE // GRID_SIZE) == (MAZE_SIZE // GRID_SIZE) - 1:
    #     visible_zones.add((grid_x + 1, grid_y))
    # if cat.y % (MAZE_SIZE // GRID_SIZE) == (MAZE_SIZE // GRID_SIZE) - 1:
    #     visible_zones.add((grid_x, grid_y + 1))

def check_victory(cat):
    """Verifica daca pisica a ajuns la final"""
    return cat.x == 0 and cat.y == 0
