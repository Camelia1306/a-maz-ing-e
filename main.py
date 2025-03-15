import pygame
import random
import time

from cat import Cat

# Dimensiuni
SCREEN_SIZE = 600
GRID_SIZE = 3  # modifica la 2, 3, 4
CELL_SIZE = SCREEN_SIZE // (GRID_SIZE * GRID_SIZE)

# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


def generate_maze(grid_size):
    """Genereaza un labirint folosind Backtracking."""
    width = height = grid_size * grid_size
    maze = [[1 for _ in range(width)] for _ in range(height)]
    stack = []
    start_x, start_y = width - 1, height - 1  # Start în dreapta jos
    maze[start_y][start_x] = 0  # Start
    stack.append((start_x, start_y))

    directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]

    while stack:
        x, y = stack[-1]
        random.shuffle(directions)
        found = False

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy // 2][x + dx // 2] = 0
                stack.append((nx, ny))
                found = True
                break

        if not found:
            stack.pop()

    return maze


def draw_maze(screen, maze):
    """Deseneaza labirintul pe ecran"""
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            color = WHITE if maze[y][x] == 0 else BLACK
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))


def draw_goal(screen):
    """Deseneaza punctul de final in coltul stanga sus"""
    pygame.draw.rect(screen, GREEN, (0, 0, CELL_SIZE, CELL_SIZE))

def draw_cat(screen, cat):
    """Deseneaza pisica in labirint"""
    pygame.draw.circle(screen, BLUE, (cat.x * CELL_SIZE + CELL_SIZE // 2, cat.y * CELL_SIZE + CELL_SIZE // 2),
                       CELL_SIZE // 3)


def check_victory(cat):
    """Verifica daca pisica a ajuns la final"""
    return cat.x == 0 and cat.y == 0


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    clock = pygame.time.Clock()
    maze = generate_maze(GRID_SIZE)

    # Punct de start in dreapta jos
    start_x, start_y = len(maze[0]) - 1, len(maze) - 1
    cat = Cat(start_x, start_y)

    # Afiseaza harta timp de 3 secunde
    screen.fill(BLACK)
    draw_maze(screen, maze)
    pygame.display.flip()
    time.sleep(3)

    running = True
    while running:
        screen.fill(BLACK)
        draw_maze(screen, maze)
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

        if check_victory(cat):
            print("Felicitari! Ai ajuns la final!")
            running = False

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
