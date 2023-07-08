import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess a number between 1 and 20: "))
        if guess < random_number:
            print("Try again. Too low")
        elif guess > random_number:
            print("Try again. Too high")

    print(f'Congrats! You guessed right ({random_number})')

#def computer_guess(x):
    #low = 1
    #high = x
    #feedback = ''
    #while feedback != 'c':
        #if low != high:
            #guess = random.randint(low, high)
        #else:
            # guess = low
        #feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower
        #if feedback == 'h':
            #high = guess - 1
        #if feedback == 'l':
            #high = guess + 1

    #print(f'The computer guessed correctly')

guess(20)