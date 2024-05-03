import pygame as pg
import sys

grid = [
    [0, 0, 9, 2, 1, 8, 0, 0, 0],
    [1, 7, 0, 0, 9, 6, 8, 0, 0],
    [0, 4, 0, 0, 5, 0, 0, 0, 6],
    [4, 5, 1, 0, 6, 0, 3, 7, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 9],
    [9, 0, 2, 3, 7, 0, 5, 0, 0],
    [6, 0, 0, 5, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 4, 9, 2, 5, 7],
    [0, 9, 4, 8, 0, 0, 0, 1, 3],
]

# start
pg.init()

# set the width and height of board
WIDTH = 550
WINDOW = pg.display.set_mode((WIDTH, WIDTH))

# set a caption to board
pg.display.set_caption("Sudoku")

# color
BACKGROUND_COLOR = (255, 255, 255)
STATIC_COLOR = (52, 31, 151)
BLACK = (0, 0, 0)
GRAY = (15, 20, 35)
# font
FONT = pg.font.SysFont('Comic Sans MS', 40)

# draw background
def draw_background():
    WINDOW.fill(BACKGROUND_COLOR)
    for i in range(0, 10):
        pg.draw.line(WINDOW, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 2)
        pg.draw.line(WINDOW, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 2)
        if i % 3 == 0:
            pg.draw.line(WINDOW, BLACK, (50 + 50 * i, 50), (50 + 50 * i, 500), 5)
            pg.draw.line(WINDOW, BLACK, (50, 50 + 50 * i), (500, 50 + 50 * i), 5)

# draw numbers
def draw_numbers():
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] != 0:
                num = FONT.render(str(grid[row][col]), True, STATIC_COLOR)
                WINDOW.blit(num, ((col + 1) * 50 + 15, (row + 1) * 50 + 15))

# draw numbers from user
def draw_numbers_from_user(position):
    x, y = position[1], position[0]
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if grid[x - 1][y - 1] != 0:
                    return
                if event.key == 48:  # checking with 0
                    grid[x - 1][y - 1] = event.key - 48
                    pg.draw.rect(WINDOW, BACKGROUND_COLOR, (position[0] * 50 + 5, position[1] * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                    pg.display.update()
                    return
                if 0 < event.key - 48 < 10:  # We are checking for valid input
                    pg.draw.rect(WINDOW, BACKGROUND_COLOR, (position[0] * 50 + 5, position[1] * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                    value = FONT.render(str(event.key - 48), True, BLACK)
                    WINDOW.blit(value, (position[0] * 50 + 15, position[1] * 50))
                    grid[x - 1][y - 1] = event.key - 48
                    pg.display.update()
                    return
                return

# draw solve button
def draw_solve_button():
    solve_text = FONT.render("Solve", True, BLACK)
    solve_rect = solve_text.get_rect(center=(WIDTH // 4, WIDTH - 30))
    pg.draw.rect(WINDOW, BACKGROUND_COLOR, solve_rect)
    WINDOW.blit(solve_text, solve_rect)

# draw reset button
def draw_reset_button():
    reset_text = FONT.render("Reset", True, BLACK)
    reset_rect = reset_text.get_rect(center=(WIDTH // 2, WIDTH - 30))
    pg.draw.rect(WINDOW, BACKGROUND_COLOR, reset_rect)
    WINDOW.blit(reset_text, reset_rect)

# draw restart button
def draw_restart_button():
    restart_text = FONT.render("Restart", True, BLACK)
    restart_rect = restart_text.get_rect(center=(3 * WIDTH // 4, WIDTH - 30))
    pg.draw.rect(WINDOW, BACKGROUND_COLOR, restart_rect)
    WINDOW.blit(restart_text, restart_rect)

# Check if a position is within the solve button
def is_solve_button_clicked(pos):
    solve_rect = pg.Rect((WIDTH // 4 - 50, WIDTH - 50, 100, 40))
    return solve_rect.collidepoint(pos)

# Check if a position is within the reset button
def is_reset_button_clicked(pos):
    reset_rect = pg.Rect((WIDTH // 2 - 50, WIDTH - 50, 100, 40))
    return reset_rect.collidepoint(pos)

# Check if a position is within the restart button
def is_restart_button_clicked(pos):
    restart_rect = pg.Rect((3 * WIDTH // 4 - 50, WIDTH - 50, 100, 40))
    return restart_rect.collidepoint(pos)

# check if the cell is empty or not
def is_empty(num):
    if num == 0:
        return True
    return False

# check if position is valid or not
def is_valid(position, num):
    # Checking row
    for i in range(0, 9):
        if grid[position[0]][i] == num:
            return False

    # Checking column
    for i in range(0, 9):
        if grid[i][position[1]] == num:
            return False

    # check the box 3*3
    x = position[0] // 3 * 3
    y = position[1] // 3 * 3

    for i in range(0, 3):
        for u in range(0, 3):
            if grid[x + i][y + u] == num:
                return False
    return True

# reset the grid to initial situation
def reset_grid():
    for i in range(0, 9):
        for u in range(0, 9):
            grid[i][u] = 0

def restart_grid():
    global grid
    grid = [
        [0, 0, 9, 2, 1, 8, 0, 0, 0],
        [1, 7, 0, 0, 9, 6, 8, 0, 0],
        [0, 4, 0, 0, 5, 0, 0, 0, 6],
        [4, 5, 1, 0, 6, 0, 3, 7, 0],
        [0, 0, 0, 0, 0, 5, 0, 0, 9],
        [9, 0, 2, 3, 7, 0, 5, 0, 0],
        [6, 0, 0, 5, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 4, 9, 2, 5, 7],
        [0, 9, 4, 8, 0, 0, 0, 1, 3],
    ]
# solve the game with backtracking algorithm
solved = 0
def sudoku_solver():
    FONT = pg.font.SysFont('Comic Sans MS', 45)
    for i in range(0, 9):
        for u in range(0, 9):
            if is_empty(grid[i][u]):
                for n in range(1, 10):
                    if is_valid((i, u), n):
                        grid[i][u] = n
                        pg.draw.rect(WINDOW, BACKGROUND_COLOR, ((u + 1) * 50 + 5, (i + 1) * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                        value = FONT.render(str(n), True, (0, 0, 0))
                        WINDOW.blit(value, ((u + 1) * 50 + 15, (i + 1) * 50 + 15))
                        pg.display.update()
                        pg.time.delay(75)

                        sudoku_solver()

                        # Exit condition
                        global solved
                        if solved == 1:
                            return

                        # if sudoku_solver returns, there's a mismatch
                        grid[i][u] = 0
                        pg.draw.rect(WINDOW, BACKGROUND_COLOR, ((u + 1) * 50 + 5, (i + 1) * 50 + 5, 50 - 2 * 5, 50 - 2 * 5))
                        pg.display.update()
                        # pygame.time.delay(50)
                return
    solved = 1

# MAIN FUNCTION
def main():
    run = True
    while run:
        for event in pg.event.get():
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                pos = pg.mouse.get_pos()
                if is_solve_button_clicked(pos):
                    sudoku_solver()
                if is_reset_button_clicked(pos):
                    reset_grid()
                if is_restart_button_clicked(pos):
                    restart_grid()
                    pg.display.update()
            if event.type == pg.QUIT:
                run = False
                sys.exit()

        draw_background()
        draw_numbers()
        draw_solve_button()
        draw_reset_button()
        draw_restart_button()

        pg.display.update()

if __name__ == "__main__":
    main()
