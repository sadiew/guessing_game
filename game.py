import random

name = raw_input("Hey there partner, what's your name?\n")
print "I've got a game for you, %s" % name
print "I'm thinking of a number between 1 and 100"
guess = int(raw_input("Try to guess the number.\n"))
our_number = random.randint(1, 100)
counter = 0

while guess in range(1,101):
    counter += 1
    if guess < our_number:
        guess = int(raw_input("Too low. Try a little higher.\n"))
    elif guess > our_number:
        guess = int(raw_input("Too high. Try a little lower.\n"))
    else:
        print "Congrats! You guessed correctly! You found my number in %d tries\n" %counter
        break 


