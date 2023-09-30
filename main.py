from prompt import get_value, get_position
from engine import add, is_game_over
from state import show


BOARD_SIZE = int(input('Enter board size(3, 4, 5): '))
grid = [ [None] * BOARD_SIZE for _ in range(BOARD_SIZE)]

print("Hi there!")
print("Welcome to XO game!!!")
USER_VALUES = {'user1': get_value()}
USER_VALUES['user2'] = 1 - USER_VALUES['user1']
turn = 'user1' if USER_VALUES['user1'] == 1 else 'user2'

show(grid)
while True:
    print(turn.upper(), 'turn')
    pos = get_position(grid)
    add(grid, USER_VALUES[turn], pos)
    show(grid)
    status = is_game_over(grid)
    if status:
        print(turn.upper(), 'won')
        break
    turn = 'user1' if turn == 'user2' else 'user2'
