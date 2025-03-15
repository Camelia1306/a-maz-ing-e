import random


def generate_maze(grid_size):
    """Genereaza un labirint folosind Backtracking"""
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
