import random
easy = random.randint (1,10)
medium = random.randint (1,20)
hard = random.randint (1,50)

guessesTaken = 0
my_name = input("Hello, What is your name? ")
difficulty = input("Well, " + my_name + ". What difficulty would you like? easy medium or hard? ")

#LEVEL IS EASY FOR GUESSING GAME
if difficulty == "easy":
    number = easy
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 10")


    flag = True
    while flag:
        guess = input('Take a guess: ')
        if guess.isdigit():
            guess = int(guess)
            flag= False
        else:
            print('Invalid input. Number allowed only! ')

    while int(guessesTaken) < 6:
        
        active = True
        while active:
            guess = input('Now that you understand the game, take a guess: ')
            if guess.isdigit():
                guess = int(guess)
                active = False    
                
            else:
                print('Invalid input. Number allowed only! ')

            guessesTaken = guessesTaken + 1
            chances = 6 - guessesTaken  
            

            if guess != easy:   
                print('That was wrong. ' + my_name + ', Try again.' )
                print(my_name + ', you have ' + str(chances) + ' guesses left. ')
            if guessesTaken == 6:
                print('Game over ' + my_name + '. You lost!!!')
                print('The number I was thinking of is ' + str(easy))        
            if guess == easy:
                break
        if guess == easy:
            guessesTaken = str(guessesTaken)
            print('You got it right, ' + my_name + '! You guessed my number in ' + guessesTaken + '  guesses!') 
            
    
#LEVEL IS MEDIUM FOR GUESSING GAME

if difficulty == "medium":
    number = medium
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 20")

    flag = True
    while flag:
        guess = input('Take a guess: ')

        if guess.isdigit():
            guess = int(guess)
            flag= False
        else:
            print('Invalid input. Number allowed only! ')

    while int(guessesTaken) < 4:
        
        active = True
        while active:
            guess = input('Now that you understand the game, take a guess: ')
            if guess.isdigit():
                guess = int(guess)
                active = False
                
            else:
                print('Invalid input. Number allowed only! ')

            guessesTaken = guessesTaken + 1
            chances = 4 - guessesTaken  
            
            if guess != medium:   
                print('That was wrong. ' + my_name + ', Try again.' )
                print(my_name + ', you have ' + str(chances) + ' guesses left. ')    
            if guessesTaken == 4:
                print('Game over ' + my_name + '. You lost!!!')
                print('The number I was thinking of is ' + str(medium))
            if guess == medium:
                break
            
        if guess == medium:
            guessesTaken = str(guessesTaken)
            print('You got it right, ' + my_name + '! You guessed my number in ' + guessesTaken + '  guesses!') 


#LEVEL IS HARD FOR GUESSING GAME

if difficulty == "hard":
    number = hard
    print ("Okay, " + my_name + ". I am thinking of a number between 1 and 50")

    flag = True
    while flag:
        guess = input('Take a guess: ')

        if guess.isdigit():
            guess = int(guess)
            flag= False
        else:
            print('Invalid input. Number allowed only! ')

    while int(guessesTaken) < 3:
        
        active = True
        while active:
            guess = input('Now that you understand the game, take a guess: ')
            if guess.isdigit():
                guess = int(guess)
                active = False
                
            else:
                print('Invalid input. Number allowed only! ')

            guessesTaken = guessesTaken + 1
            chances = 3 - guessesTaken  
            
            if guess != hard:   
                print('That was wrong. ' + my_name + ', Try again.' )
                print(my_name + ', you have ' + str(chances) + ' guesses left. ')    
            if guessesTaken == 3:
                print('Game over ' + my_name + '. You lost!!!')
                print('The number I was thinking of is ' + str(hard))
            if guess == hard:
                break
            
        if guess == hard:
            guessesTaken = str(guessesTaken)
            print('You got it right, ' + my_name + '! You guessed my number in ' + guessesTaken + '  guesses!') 

