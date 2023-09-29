import os

def clear_screen():
    os.system('clear')


def represent(el):
    if el == 1:
        return ' X '
    if el == 0:
        return ' O '
    return '   '

def show(grid):
    clear_screen()
    print('-' * 13)
    for line in grid:
        print('|', end='')
        print('|'.join(map(represent, line)), end='')
        print('|')
        print('-' * 13)