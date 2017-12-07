# loops example
# running total
# Ken Averitt
# 10/6

# use a loop to calculate the remaining running total

def main():

    runningTotal = 0
    keepGoing = True



    while keepGoing:
        # keep going until the user types a negative
        # number
        print("Enter a number: ")
        number = int(input('> '))
        if number < 0:
            # end the loop
            keepGoing = False
        else:
            # add the number to the total
            # runningTotal = runningTotal + number
            runningTotal += number
    # print the total
    print("Total is: ",runningTotal)




# start
main()
