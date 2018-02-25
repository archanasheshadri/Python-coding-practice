#author Archana
'''
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl',
then your program should print
Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc

'''



def isMinMax(string,letter):
    '''
    string: string with variable length

    returns: True if string is in alphabetical order and False otherwise.
    '''
    if len(string) > 1:
        return string[len(string)-1] <= letter
    else:
        return string <= letter


count = 0
s = 'zyxwvutsrqponmlkjihgfedcba'
temp = ''
string = s[0]

for letter in s:
    if count == 0:
        letter = s[1]       ### To point letter to the second character of the string
    checked = isMinMax(string, letter)
    if checked and count != 0:
        string += letter    ## If the characters are in alphabetical order, append each letter read to the variable 'string'
        if len(string) == len(s):   ## To check if all the characters in the variable 's' are in alphabetical order
            temp = string
    elif len(string) > len(temp) and count != 0:
        temp = string       ## Place the longest alphabetical substring in 'temp'
        string = letter     ## Initialize the variable 'string' to the present letter once the alphabetical substring is found 
    elif count != 0:       
        string = letter     ## Initialize the variable 'string' to the present letter once the alphabetical substring is found 
        
    count += 1

if len(string) > len(temp) and checked:  ## Check for longest substring at the end of the actual string 's'(Boundary check)
    temp = string
        
    
print 'Longest substring in alphabetical order is: ' + str(temp)




##Edx answer
curString = s[0]
longest = s[0]
for i in range(1, len(s)):
    if s[i] >= curString[-1]:
        curString += s[i]
        if len(curString) > len(longest):
            longest = curString
    else:
        curString = s[i]
print 'Longest substring in alphabetical order is:', longest
