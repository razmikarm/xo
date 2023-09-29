import os

def clear_screen():
    if os.name == 'posix':
        os.system("clear")
    else:
        os.system("cls")


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