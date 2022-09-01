print("Ходы принимаются в формате [0][0] = 'X' или [1][1] = 'О'")
print("Крестик - латинская буква X, нолик - латинская буква O")

game_matrix = [[None, None, None], [None, None, None], [None, None, None]]
game_is_on = True

board = range(1, 10)
def draw_board(board):
    print("-------------")
    for i in range(3):
        print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("-------------")
draw_board(board)

while game_is_on:
    move = input()
    exec("game_matrix" + move)
    for row in game_matrix:
        print(row)

    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Game over!")
            game_is_on = False
            break
            game_is_on = False
            break