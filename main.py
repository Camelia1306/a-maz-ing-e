import pygame
import time
from cat import Cat
from game import draw_maze, draw_cat, draw_goal, check_victory, update_visible_zones
from maze import generate_maze

# Dimensiuni
SCREEN_SIZE = 600
GRID_SIZE = 3  # modifica la 2, 3, 4
CELL_SIZE = SCREEN_SIZE // (GRID_SIZE * GRID_SIZE)
MAZE_SIZE = GRID_SIZE * GRID_SIZE  # Dimensiunea totala a labirintului

# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()
    maze = generate_maze(GRID_SIZE)

    # Punct de start in dreapta jos
    start_x, start_y = len(maze[0]) - 1, len(maze) - 1
    cat = Cat(start_x, start_y)

    visible_zones = set()
    update_visible_zones(cat, visible_zones)

    # Arata harta hint la inceput
    screen.fill(BLACK)
    draw_maze(screen, maze, {(x, y) for x in range(GRID_SIZE) for y in range(GRID_SIZE)})
    pygame.display.flip()
    time.sleep(3)

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze(screen, maze, visible_zones)
        draw_goal(screen)
        draw_cat(screen, cat)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    cat.move(0, -1, maze)
                elif event.key == pygame.K_DOWN:
                    cat.move(0, 1, maze)
                elif event.key == pygame.K_LEFT:
                    cat.move(-1, 0, maze)
                elif event.key == pygame.K_RIGHT:
                    cat.move(1, 0, maze)
                update_visible_zones(cat, visible_zones)


        if check_victory(cat):
            print("Felicitari! Ai ajuns la final!")
            running = False

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
