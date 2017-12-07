# feet to inches converting
# 11/11/17
# CTI 110 M6T2_FeetToInches
# Ken Averitte
#

# if 1 foot = 12 inches
# then 3 feet = ?

def feetToInches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

def main ():
    userFeet = float( input( "Please enter the number of feet: " ))
    print()
    inches = feetToInches( userFeet )
    print( userFeet, " feet converted to inches is", format( inches, ".2f" ), "inches" )

main()
