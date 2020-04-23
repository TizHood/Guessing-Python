import random
easy = random.randint (1,10)
medium = random.randint (1,20)
hard = random.randint (1,50)

guessesTaken= 0
my_name = input("Hello, What is your name? ")
difficulty = input("Well, " + my_name + ". What difficulty would you like? easy medium or hard? ")
if difficulty == "medium":
    number = medium
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20")
    
while guessesTaken < 3:
    guess = int(input('Take a guess: '))
    guessesTaken = guessesTaken + 1
    
    if guess != number:   
        print('That was wrong. ' + my_name + ', Try again.' )    
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + my_name + '! You guessed my number in ' + guessesTaken + '  guesses!') 
