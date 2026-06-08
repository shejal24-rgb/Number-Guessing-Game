import random

number = random.randint(11, 99)

print("Guess the number (11 to 99)")
print("You have 3 chances!")

for i in range(3):

    guess = int(input("Enter your guess: "))

    if guess == number:
        print("You win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")
    
else:
    print("You Lost :(")
    print("Number was:", number)
    