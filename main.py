import pygame
import os

pygame.init()
pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NAVY = (17, 25, 33)
LIGHT_BLUE = (100, 127, 143)
BLUE = (41, 54, 66)

WIDTH, HEIGHT = 600, 700

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.init()
pygame.display.set_caption("Tic Tac Toe")

result_font = pygame.font.Font(os.path.abspath('Montserrat-Regular.ttf'), 90)
reset_font = pygame.font.Font(os.path.abspath('Montserrat-Regular.ttf'), 55)

SQUARE_SIZE = 200

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

cross = pygame.image.load(os.path.abspath('cross.png'))
nought = pygame.image.load(os.path.abspath('nought.png'))

taken_squares = []

turn = "X"

result = 0  # 0 means no result, 1 means crosses win, 2 means noughts win, and 3 means it's a draw
print_result = ""


def reset_board():
    global board, result, turn, print_result, taken_squares

    board = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    result = 0
    turn = "X"
    print_result = ""
    taken_squares = []


def game_result():
    global print_result, board

    if result == 1:
        print_result = "Crosses Win"
    elif result == 2:
        print_result = "Noughts Win"
    elif result == 3:
        print_result = "Draw"

    shadow_surface = result_font.render(print_result, False, BLACK)
    shadow_rect = shadow_surface.get_rect(center=((WIDTH // 2) - 5, ((HEIGHT - 100) // 2) - 3))

    text_surface = result_font.render(print_result, False, WHITE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, (HEIGHT - 100) // 2))

    WINDOW.blit(shadow_surface, shadow_rect)
    WINDOW.blit(text_surface, text_rect)


# ----- Game loop -----

clock = pygame.time.Clock()

while True:

    clock.tick(60)
    WINDOW.fill(NAVY)

    for event in pygame.event.get():
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # If the grid is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse_y <= 600:
            col = mouse_x // SQUARE_SIZE
            row = mouse_y // SQUARE_SIZE
            # If left or right clicked and the square is empty and it is your turn, you can draw an X or O
            if event.button == 1 and board[col][row] not in taken_squares and turn == "X" and result == 0:
                turn = "O"
                board[col][row] = 1
                taken_squares.append(board[col][row])
            elif event.button == 3 and board[col][row] not in taken_squares and turn == "O" and result == 0:
                turn = "X"
                board[col][row] = 2
                taken_squares.append(board[col][row])
        # If button is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN and 225 < mouse_x < 350 and 625 < mouse_y < 675:
            reset_board()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset the board
                reset_board()

    for row in range(3):
        for col in range(3):
            grid_rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)  # Draw the grid
            pygame.draw.rect(WINDOW, BLUE, grid_rect, 3)

            if board[col][row] == 1:  # Draw a cross
                WINDOW.blit(cross, (col * SQUARE_SIZE, row * SQUARE_SIZE))

            if board[col][row] == 2:  # Draw a nought
                WINDOW.blit(nought, (col * SQUARE_SIZE, row * SQUARE_SIZE))

            # Check for a winner

            if board[col][0] == board[col][1] == board[col][2] and board[col][0] != 0:  # Check for vertical winner
                result = board[col][0]

            if board[0][row] == board[1][row] == board[2][row] and board[0][row] != 0:  # Check for horizontal winner
                result = board[0][row]

            if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:  # Check for diagonal winner
                result = board[0][0]
            if board[2][0] == board[1][1] == board[0][2] and board[2][0] != 0:
                result = board[2][0]

    if len(taken_squares) == 9 and result == 0:
        result = 3  # Draw

    # Bottom menu

    bottom_rect = pygame.Rect(0, 600, WIDTH, HEIGHT - 600)
    pygame.draw.rect(WINDOW, BLUE, bottom_rect)  # Draw the menu at the bottom

    button_rect = pygame.Rect(225, 625, 150, 50)
    pygame.draw.rect(WINDOW, NAVY, button_rect, 0, 5)
    text_surface = reset_font.render("Reset", False, LIGHT_BLUE)
    text_rect = text_surface.get_rect(center=(WIDTH // 2, 650))
    WINDOW.blit(text_surface, text_rect)

    game_result()

    pygame.display.update()
