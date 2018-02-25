##Iterative method to find the length of the string
#def lenIter(aStr):
#    '''
#    aStr: a string
#    
#    returns: int, the length of aStr
#    '''
#    ans = 0
#    for letter in aStr:
#        ans += 1
#   return ans




##Recursive method

def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    
    if aStr == '':
        return 0
    return lenRecur(aStr[1:]) + 1
    
    
    
