import random


def play():
    game_options = ["r", "p", "s"]
    mychoice = input("Your turn! Rock (r), Paper (p), or Scissors (s)?: ")
    compchoice = random.choice(game_options)

    if mychoice == compchoice:
        return "It\'s a tie"

    if is_win(mychoice, compchoice):
        return "You won!"

    return "You lost!"



def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True

'''
def tie_replay():
    replay = play()
    if replay == "It\'s a tie":
        print(play())

    else:
        print(replay)

tie_replay()
'''

print(play())