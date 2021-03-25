import random

def guess(x):
    random_number = random.randint(1, x);
    guess = 0
    end = False

    while guess != random_number and end != True:
        guess = input(f"Guess a number between 1 and {random_number}")
        if guess.isnumeric() == False:
            print ("Please enter a number")
            guess = 0
            continue
        guess = int(guess)
        if guess < random_number:
            print ("Guess is too low.")
            # play_again = input("Play again. Enter any number if yes and N if no")
        elif guess > random_number:
            print ("Guess is too high.")
            # play_again = input("Play again. Enter any number if yes and N if no")
        if guess != random_number:
            play_again = input("Hit N to end game else any key")
            if play_again == 'N':
                    end = True
    if end == True:
        print(f"Thanks for playing. The number was {random_number}")
    else:
        print (f"Yay congrats. Ypu have guessed the number {random_number} correctly")

def my_custom_random(exclude, x, y):
  randInt = random.randint(x,y)
  return my_custom_random(exclude, x, y) if randInt in exclude else randInt 


def computer_guess(x):
    guess = int(input(f"Guess a number between 1 and {x}"))
    selected = []
    high = x
    low = 0
    feedback = ''
    computer_guess = random.randint(1, x)

    if guess in range(1, x):
        new_guess = 0
        print(f"Computer guess is {computer_guess}")

        feedback = input(f"Is it high (h) low(l) or correct(c)").lower()
        while feedback != 'c':
            if feedback == 'h':
                if computer_guess > high:
                    continue
                else:
                    high = computer_guess - 1
                
            elif feedback == 'l':
                if computer_guess < low:
                    continue
                else:
                    low = computer_guess + 1
            if low != high:
                new_guess = random.randint(low, high)
            else:
                new_guess = low
            
            computer_guess = new_guess
            print(f"Computer guess is {computer_guess}")

            feedback = input(f"Is it high (h) low(l) or correct(c)").lower()

        print(f"Yay got the number {guess}")
    else:
        print(f"Number must be in range 1 and {x}")

if __name__ == '__main__':
    
    computer_guess(10)


        
