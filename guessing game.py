import random

secret = random.randrange(1, 101)

guess = 0
tries = 0
while guess != secret:
    guess = int (input("Make a guess: "))
    tries = tries + 1

    if guess > secret:
        print("too high")
    elif guess < secret:
        print("too low!")
    else:
        print("you got it!")

    print("number of tries:", tries)
