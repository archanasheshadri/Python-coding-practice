#def recurPower(base, exp):
#    """assumes that n is an int > 0
#       returns n!"""
#    if exp <= 0:
#        return 1
#    elif exp == 1:
#        return base
#    return base*recurPower(base,exp-1)



def recurPowerNew(base, exp):
    '''
    base^exp = (base^2)^exp/2       if exp > 0 and exp is even
    base^exp = base * base^(exp-1)  if exp > 0 and exp is odd
    base^exp = 1                    if exp = 0
    '''
   
    if exp == 0:                         # Base case is when exp = 0
        return 1
    
    elif exp % 2 == 0:                   # Recursive case 1: exp > 0 and even
        return recurPowerNew(base*base, exp/2)

    return base*recurPowerNew(base,exp-1)# Otherwise, exp must be > 0 and odd, so use the second
                                         #  recursive case.




