def get_value():
    while True:
        string = input("Enter your letter (X or O): ").upper()
        if string in ('X', 'O'):
            return int(string == 'X')
        else:
            print("The letter is not valid. Reenter your letter (X or O): ")

def get_position(grid):
    while True:
        num = input(
            'Enter the position (1-9) where you want to insert your letter: ')
        if len(num) == 1 and num in '123456789':
            num = int(num)
            line_idx = (num - 1) // 3
            el_idx = (num - 1) % 3
            if grid[line_idx][el_idx] is None:
                return num
            else:
                print("The position is already used")
                continue
        else:
            print("The position is not valid")
            continue