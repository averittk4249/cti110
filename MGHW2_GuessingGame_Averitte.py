# guessing game python
# 10/11/17
# CTI-110 M6HW2 - Random Number Guessing Game
# Ken Averitte
#

import random

def generateRandomNumber():
    randomNumber = random.randInt( 1, 100 )
    return randomNumber

def askUserForNumber( message = "Guess the number: " ):
    userNumber = int(input( message ))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

def main():
    userCongratulated = False
    letsStart = True

    while userCongratulated or letsStart:
        randomNumber = generateRandomNumber()
        print( "For testing purposes, random number: ", randomNumber )
        userNumber = askUserForNumber()
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message )
            userNumber = askUserForNumber( "Try again: " )
            message = checkUserNumber( userNumber, randomNumber )

        print( message )
        userCongratulated = True

main()
     
