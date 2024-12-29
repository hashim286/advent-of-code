# A and X give rock, B and Y give paper, C and Z give scissors

points_for_rock = 1
points_for_paper = 2
points_for_scissors = 3

points_for_win = 6
points_for_draw = 3
points_for_loss = 0

player_score = 0

FILE_PATH = "text.txt"


def translate_move_to_number(move):
    if move == "A" or move == "X":
        return points_for_rock
    elif move == "B" or move == "Y":
        return points_for_paper
    else:
        return points_for_scissors


def determine_winner(move_one, move_two):
    # if difference between the moves is 1, the first move wins, if difference is 2, second move wins
    if move_two - move_one == 1 or move_one - move_two == 2:
        return points_for_win
    elif move_two == move_one:
        return points_for_draw
    else:
        return points_for_loss


with open(FILE_PATH) as file:
    for line in file:
        moves = line.split(" ")
        moves[1] = moves[1].strip()
        opponent_move = translate_move_to_number(moves[0])
        your_move = translate_move_to_number(moves[1])
        player_score += determine_winner(opponent_move, your_move) + your_move
    print(player_score)

