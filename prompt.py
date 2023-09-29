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
    num= int(input('Enter the position (1-9) where you want to insert your letter: '))
    while True:
        if num in range(1,10):
            line_idx = (num - 1) // 3
            el_idx = (num - 1) % 3
        elif grid[line_idx][el_idx] is not None:
            position = num
            break
        else: 
            num=int(input('The position is not valid. Enter another position (1-9): '))
            continue

    return position