import random

print("Number Guessing Game")
number = random.randint(1,9)
chances = 0
print("Guess a number between 1 to 9")

while chances < 5:
    guess = int(input("Enter your guess"))
    if(guess == number):
        print("Congratulations!! YOU WON")
        break
    elif(guess < number):
        print("You are below the number. Keep Trying!")
    else:
        print("You are above the number. Keep Trying!")
    chances = chances + 1
if not chances < 5:
    print("You Lose. The number is",number)