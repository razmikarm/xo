def get_value():
    string = input("Enter your letter (X or O): ")
    while True:
        if string not in 'XxOo':
            string = input(
                "The letter is not valid. Reenter your letter (X or O): ")
            continue
        else:
            if string in 'Xx':
                value = 1
            else:
                value = 0
            break

    return value


def get_position(grid):
    while True:
        num = input(
            'Enter the position (1-9) where you want to insert your letter: ')
        if len(num) == 1 and num in '123456789':
            num = int(num)
            line_idx = (num - 1) // 3
            el_idx = (num - 1) % 3
            if grid[line_idx][el_idx] is not None:
                return num
            else:
                print("The position is already used")
                continue
        else:
            print("The position is not valid")
            continue
