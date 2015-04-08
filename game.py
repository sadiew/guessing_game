import random

name = raw_input("Hey there partner, what's your name?\n")
print "I've got a game for you, %s" % name
print "I'm thinking of a number between 1 and 100. Try to guess the number."

our_number = random.randint(1, 100)
counter = 0
scores = []

while True:
    try: 
        guess = int(raw_input("Your guess? "))
        counter += 1
        if guess not in range(1,101):
            guess = int(raw_input("Guess out of bounds. Your new guess? "))
            counter += 1
    except:
        guess = int(raw_input("Did you even read the instructions?!?! Let's try that again. Pick a NUMBER between 1 and 100? "))
        counter += 1
    
    if guess < our_number:
        print "Too low. Try a little higher."
    elif guess > our_number:
        print "Too high. Try a little lower."
    else:
        print "Congrats! You guessed correctly! You found my number in %d tries\n" %counter
        scores.append(counter)
        counter = 0 
        answer = raw_input("Do you want to play again? Y/N ")
        our_number = random.randint(1, 100) 
        if answer == 'N':
            break

print "Your best score was: " + str(min(scores))



