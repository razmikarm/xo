def represent(el):
    if el == 1:
        return ' X '
    if el == 0:
        return ' O '
    return '   '

def show(grid):
    for line in grid:
        print('|'.join(map(represent, line)))




