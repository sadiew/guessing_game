import random

name = raw_input("Hey there partner, what's your name?\n")
print "I've got a game for you, %s" % name
print "I'm thinking of a number between 1 and 100. Try to guess the number."

our_number = random.randint(1, 100)
counter = 0

while True:
    guess = int(raw_input("Your guess? "))
    counter += 1
    if guess < our_number:
        print "Too low. Try a little higher."
    elif guess > our_number:
        print "Too high. Try a little lower."
    else:
        print "Congrats! You guessed correctly! You found my number in %d tries\n" %counter
        break 


