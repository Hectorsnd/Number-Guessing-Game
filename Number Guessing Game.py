import random

while True:
    number = input('Type a number: ')
    if number.isdigit():
        number = int(number)
        if number <= 0:
            print('Please type a number larger than 0 next time')
            continue
    else:
        print('Please type a number next time')
        continue
    break

random_number = random.randint(0, number)
guesses = 0

while True:
    guesses += 1

    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time')
        continue

    if user_guess == random_number:
        print('You got it!')
        break
    elif user_guess > random_number:
        print('You were above the number')
    else:
        print('you were below the number')

print('You got it in', guesses, 'guesses')