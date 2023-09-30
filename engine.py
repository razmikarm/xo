def add(grid, value, position):
    """
        Positions

        [1, 2, 3]
        [4, 5, 6]
        [7, 8, 9]
    """
    line_idx = (position - 1) // 3
    el_idx = (position - 1) % 3
    if grid[line_idx][el_idx] is not None:
        raise Exception('The field is not empty')
    grid[line_idx][el_idx] = value

def is_game_over(grid):
    if (grid[0][0] == grid[1][1] == grid[2][2] or grid[0][2] == grid[1][1] == grid[2][0]) and grid[1][1] is not None:
        return True
    for column in zip(*grid):
        if column[0] is not None and len(set(column)) == 1:
            return True
    for row in grid:
        if row[0] is not None and len(set(row)) == 1:
            return True
    for i in range(len(grid)):
        if None in grid[i]:
            return False
    return True
