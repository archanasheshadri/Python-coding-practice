school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
       or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1

print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)



#Finding vowel function

def isVowel2(char):
    '''
    char: a single letter of any case

    returns: True if char is a vowel and False otherwise.
    '''
    char = char.lower()
    return (char in 'aeiou')
