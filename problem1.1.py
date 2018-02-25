#def isVowel(char):
#    '''
#    char: a single letter of any case

#    returns: True if char is a vowel and False otherwise.
#    '''
#    char = char.lower()
#    return (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u')

#count = 0
#s = 'aecbobobegghakl'
#for letter in s:
#    vowel = isVowel(letter)
#    if vowel:
#        count += 1
#print 'Number of vowels: ' + str(count)



def isBob(string):
    '''
    string: string with three characters

    returns: True if string is 'bob' and False otherwise.
    '''
    return (string[0] == 'b' and string [1] == 'o' and string[2] == 'b')
        
 

count = 0
s = 'aecbobobobeggboblegbob'
string = ''


for letter in s:
    string += letter
    if len(string) == 3:
        check = isBob(string)
        if check:
            count += 1
        if string[2] == 'b':
            string = 'b'
        elif string.count('bo') > 0:
            string = 'bo'
        else:
            string = ''

print 'Number of times bob occurs is: ' + str(count)
            
        
