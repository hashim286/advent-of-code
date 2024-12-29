# X means you need to lose, Y means need draw, Z means you win

points_for_rock = 1
points_for_paper = 2
points_for_scissors = 3

points_for_win = 6
points_for_draw = 3
points_for_loss = 0

player_score = 0


FILE_PATH = "text.txt"

def translate_move_to_number(move):
    if move == "A":
        return points_for_rock
    elif move == "B":
        return points_for_paper
    else:
        return points_for_scissors


def determine_complement_move(move, condition):
    if condition == "X":
        move -= 1
        if move == 0:
            return points_for_scissors
        elif move == 1:
            return points_for_rock
        else:
            return points_for_paper
    elif condition == "Y":
        return move
    elif condition == "Z":
        move -= 1
        if move == 0:
            return points_for_paper
        elif move == 1:
            return points_for_scissors
        else:
            return points_for_rock


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
        text = line.split(" ")
        text[1] = text[1].strip()
        # text[0] is opponent move, text[1] is game outcome
        opponent_move = translate_move_to_number(text[0])
        your_move = determine_complement_move(opponent_move, text[1])
        player_score += determine_winner(opponent_move, your_move) + your_move
    print(player_score)


