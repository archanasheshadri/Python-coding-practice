#GCD in iterative way


#My approach
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a > b:
        if a%b == 0:
            return b
        small = b
        while small > 1:
            small -= 1
            if a%small == 0 and b%small == 0:
                return small
    else:
        if b%a == 0:
            return a
        small = a
        while small > 1:
            small -= 1
            if b%small == 0 and a%small == 0:
                return small


    if a%small != 0 or b%small != 0:
        return 1

##Best Approach
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''

    testValue = min(a, b)

    # Keep looping until testValue divides both a & b evenly
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1

    return testValue





#Recursive code

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return b
    else:
        return gcdRecur(b, a%b)
    



