# M3H1 Age Classifier
# 11/19/17
# Ken Averitte
# Age Classifier Python

userAge = int( input( "Please enter your age: " ) )

if userAge <= 1:
    print( "You are an infant" )
elif userAge < 13:
    print( "You are a child" )
elif userAge < 20:
    print( "You are a teenager" )
elif userAge >= 20:
    print( "You are an adult" )
