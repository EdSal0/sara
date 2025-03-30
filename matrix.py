import curses
import random
import time

def matrix_effect(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(50)
    max_y, max_x = stdscr.getmaxyx()
    columns = [0] * max_x
    start_time = time.time()
    
    while time.time() - start_time < 5:
        stdscr.clear()
        for i in range(min(max_x, len(columns))):
            if random.random() < 0.1:
                columns[i] = 0
            if columns[i] < max_y - 1:  # Evita exceder los límites
                char = chr(random.randint(33, 126))  # Caracteres imprimibles aleatorios
                try:
                    stdscr.addstr(columns[i], i, char, curses.color_pair(1))
                except curses.error:
                    pass  # Evita errores si la terminal es muy pequeña
                columns[i] += 1
        stdscr.refresh()
        time.sleep(0.05)

def effect():
    curses.wrapper(matrix_effect)
