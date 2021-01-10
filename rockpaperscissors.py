# Importing Time Library as the Variable t
import time as t 

# Function that Names the Players and passes them to the main Function 
def naming():
    player1 = input('\n Enter Your Nickname Player 1: ')
    player2 = input('\n Enter Your Nickname Player 2: ')
    main(player1 , player2)

# Main Function
def main(player1 , player2):
    # Score and Counter Setup
    roundTimes = dict()
    roundNumber = 1
    options = ['rock' , 'paper' , 'scissors']
    p1Wins = 0
    p2Wins = 0
    p1Score = 0
    p2Score = 0
    print('\nWelcome to RockPaperScissors')
    t.sleep(3)
    print('Countdown is Beginning...')
    t.sleep(1)
    print(3)
    t.sleep(1)
    print(2)
    t.sleep(1)
    print(1)
    # Main While Loop
    while 1:
        start = t.time()
        print(f'\n{player1} Wins: {p1Wins}')
        print(f'{player2} Wins: {p2Wins}')

        # If you Dont Pick Rock Paper or Scissors you cant Continue 
        while 1:
            choice1 = input(f'\nIts your turn {player1}: Rock , Paper , Scissors?: ')
            if not choice1.lower() in options:
                print('Not an Option :/')
                continue
            break
        
        # If you Dont Pick Rock Paper or Scissors you cant Continue 
        while 1: 
            choice2 = input(f'\nIts your turn {player2}: Rock , Paper , Scissors?: ')
            if not choice2.lower() in options:
                print('Not an Option :/')
                continue
            break
        print(3)
        t.sleep(1)
        print(2)
        t.sleep(1)
        print(1)
        t.sleep(1)
        # If its a Draw , Print Its a Draw :O
        if choice1.lower() == 'rock' and choice2 == 'rock':
            print('Its a Draw :O \n')
        elif choice1.lower() == 'paper' and choice2 == 'paper':
            print('Its a Draw :O \n')
        elif choice1.lower() == 'scissors' and choice2 == 'scissors':
            print('Its a Draw :O \n')
        # If Player 1 Wins , Print Player 1 Wins and Add a Score
        elif choice1.lower() == 'rock' and choice2 == 'scissors':
            print(f'\n{player1} Wins This Round!')
            p1Score += 1
        elif choice1.lower() == 'paper' and choice2.lower() == 'rock':
            print(f'\n{player1} Wins This Round!')
            p1Score += 1
        elif choice1.lower() == 'scissors' and choice2.lower() == 'paper':
            print(f'\n{player1} Wins This Round!')
            p1Score += 1
        # If its not a Draw and Player 1 Didnt Win.. Player 2 Wins
        else:
            print(f'\n{player2} Wins This Round!')
            p2Score += 1

        # Print Score
        print(f'\n{player1} Score is {p1Score}')
        print(f'{player2} Score is {p2Score}')
        
        end = t.time()
        # roundTimes is a Dictionary ( Holds Key : Value Pairs ) .. I take the end time from the start time and assign it to the round Key
        roundTimes[f"round{roundNumber}"] = end - start
        # Update Round number to make a new Dictionary Key next time for its Value ( Time )
        roundNumber = int(roundNumber) + 1

        # If either Player 1 or Player 2 Wins , Print the roundTimes Key : Value Pairs, and Add a Win to their Win Counter
        # If playAgain == y , Reset the Scores and 'continue' restarts the Main While Loop , if playAgain == n , Exit the Game
        if p1Score == 3:
            print(f'\n{player1} Wins :D Congratulations!')
            print('Here is the Time Spent in Each Round: ')
            for x,y in roundTimes.items():
                print('Time spent in' , x,y)
            playAgain = input('Would You Like To Play Again?: (y/n) ')
            if playAgain == 'y':
                p1Wins +=1
                p1Score = 0
                p2Score = 0
                continue
            elif playAgain == 'n':
                exit()
            else:
                playAgain = input("Your Options for Playing Again are y/n?: ")

        elif p2Score == 3:
            print(f'{player2} Wins :D Congratulations! \n')
            print('Here is the Time Spent in Each Round: ')
            for x,y in roundTimes.items():
                print('Time spent in' , x,y)
            playAgain = input('Would You Like To Play Again?: (y/n) ')
            if playAgain == 'y':
                p2Wins += 1
                p1Score = 0
                p2Score = 0
                continue
            elif playAgain == 'n':
                exit()
            else:
                playAgain = input("Your Options for Playing Again are y/n?: ")



# Calling the Function to Begin 
naming()