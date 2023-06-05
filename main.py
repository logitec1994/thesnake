import os
import time

import random

import getch

# Variables
game_condition = True
rows = 15
cols = 45
player_score = 0
player_current_position = [1, 4]
goal_current_position = [0, 0]


matrix = [[" "] * cols for _ in range(rows)]

# Functions
def reverse_game_condition():
    global game_condition
    if game_condition == True:
        game_condition = False

def upd_score():
    global player_score
    player_score += 1

def start_position_field():
    for i, x in enumerate(matrix):
        for j, y in enumerate(x):
            if i == 0 and j >= 0:
                matrix[i][j] = "X"
            if i >= 0 and j == 0:
                matrix[i][j] = "X"
            if i <= rows-1 and j == cols-1:
                matrix[i][j] = "X"
            if i == rows-1 and j <= cols-1:
                matrix[i][j] = "X"

def start_position_player(posx, posy):
    matrix[posx][posy] = "P"

def start_goal_position(posx, posy):
    matrix[posx][posy] = "G"

def move_goal():
    global goal_current_position
    goal_current_position = [random.randint(1, rows-2), random.randint(1, cols-2)]

def move_player():
    global player_current_position
    player_current_position = [random.randint(1, rows-2), random.randint(1, cols-2)]
    
def score(player_name: str, score: int):
    print(f"The player - {player_name} has {score} points")
    print()

def get_user_name():
    return input("Please enter your name: ")

def render_field():
    for row in matrix:
        print(" ".join(str(element) for element in row))

def p_indexes():
    global rows
    global cols

    index_of_p = ()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "P":
                index_of_p = (i, j)
    
    return index_of_p

def g_indexes():
    global rows
    global cols

    index_of_g = ()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "G":
                index_of_g = (i, j)
    
    return index_of_g

def move():
    choise = getch.getch()
    # choise = random.choice("awsd")
    match choise:
        case "a": player_current_position[1] -= 1
        case "d": player_current_position[1] += 1
        case "w": player_current_position[0] -= 1
        case "s": player_current_position[0] += 1
    
    print("Last move was:", choise)

player_name = get_user_name()

def render_game():
    os.system("clear")
    score(player_name=player_name, score=player_score)
    start_position_field()
    start_goal_position(goal_current_position[0], goal_current_position[1])
    start_position_player(player_current_position[0], player_current_position[1])
    render_field()

move_player()
move_goal()

while game_condition:
    matrix = [[" "] * cols for _ in range(rows)]
    render_game()
    print("Make your move (WASD controls)")
    time.sleep(0.2)
    if g_indexes() == ():
        move_goal()
        print(goal_current_position)
        start_goal_position(goal_current_position[0], goal_current_position[1])
        upd_score()
        render_game()
        print("Make your move (WASD controls)")
    if (player_current_position[0] < 1 or player_current_position[0] >= rows-1)\
        or (player_current_position[1] < 1 or player_current_position[1] >= cols-1):
        os.system("clear")
        game_condition = False
        print("Game over!")
        print("Final resul below")
        print(" |")
        print("\|/")
        score(player_name=player_name, score=player_score)
        break
    move()
