import time
import curses

# For The Snake game
from src import menu, game

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    current_row_idx = 0
    
    menu.print_menu(stdscr, current_row_idx)
    while True:
        key = stdscr.getch()
        stdscr.clear()
                
        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < len(menu.menu) - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if current_row_idx == len(menu.menu) - 1:
                break
            if current_row_idx == 1:
                game.print_game(stdscr)
            else:
                stdscr.addstr(0, 0, f"You presser {menu.menu[current_row_idx]}")
                stdscr.getch()
        menu.print_menu(stdscr, current_row_idx)
        stdscr.refresh()
    
curses.wrapper(main)