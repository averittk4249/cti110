# Determing test averages and grades
# 11/6/17
# CTI-110 M6HW1 - Test Average and Grade
# Ken Averitte


def calcAverage( score1, score2, score3, score4, score5):
    average = ( score1 + score2 + score3 + ccore4 + score5)/5
    return average

def determineGrade( userScore):
    if( userScore < 60):
        return "F"
    elif( userScore < 70):
        return "D"
    elif( userScore < 80):
        return "C"
    elif( userScore < 90):
        return "B"
    elif( userScore < 101):
        return "A"
    
def askForScores():
    score1 = float( input( "Please enter score 1: "))
    score2 = float( input( "Please enter score 2: "))
    score3 = float( input( "Please enter score 3: "))
    score4 = float( input( "Please enter score 4: "))
    score5 = float( input( "Please enter score 5: "))

    return score1, score2, score3, score4, score5

def printTableofResults(score1, score2, score3, score4, score5):
    print( "Score\tLetter Grade" )
    print(str( score1 ) + "\t\t" + determineGrade( score1 ), \
          str( score2 ) + "\t\t" + determineGrade( score2 ), \
          str( score3 ) + "\t\t" + determineGrade( score3 ), \
          str( score4 ) + "\t\t" + determineGrade( score4 ), \
          str( score5 ) + "\t\t" + determineGrade( score5 ), sep = "\n" )

def main():
    score1, score2, score3, score4, score5 = askForScores()
    print()
    printTableofResults( score1, score2, score3, score4, score5 )

main()

    
    
    
