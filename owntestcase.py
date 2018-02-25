'''
Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:
'''

def f(s):
    return 'b' in s



def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    
    tempL = L[:]
    for string in tempL:
        if not f(string):
            L.remove(string)
    return len(L)

    

#run_satisfiesF(L, satisfiesF)




