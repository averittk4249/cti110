# Factorial - python
# m5hw3 Factorial
# 11/20/17
# Ken Averitte
#

number =   input( "Enter a non-negative integer to take the factorial of: " )

product = 1
for i in range( number ):
    product = product * ( i + 1 )

print( product )
