import random

def play():
    print("Rock Paper Scissors!")
    user = input("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "Tied."
    
    if is_win(user, computer):
        return 'You won!'
    
    if is_lost(user, computer):
        return 'You lost.'
    
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') (player == 'p' and opponent == 'r'):
        return True
    
def is_lost(player, opponent):
    if (player == 's' and opponent == 'r') or (player == 'p' and opponent == 's') (player == 'r' and opponent == 'p'):
        return True
    
print(play())