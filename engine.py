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

