def isBob(string):
    '''
    string: string with three characters

    returns: True if string is 'bob' and False otherwise.
    '''
    return (string[0] == 'b' and string [1] == 'o' and string[2] == 'b')


count = 0
s = 'bobebobbbobbboboboobobyhbobobxiszokbobbo'
string = ''
i=0
j=2
while j < len(s):
    string = s[i] + s[i+1] + s[j]
    check = isBob(string)
    if check:
        count += 1
    i += 1
    j += 1
print 'Number of times bob occurs is: ' + str(count)


#Edx answer
numBobs = 0
for i in range(1, len(s)-1):
    if s[i-1:i+2] == 'bob':
        numBobs += 1
print 'Number of times bob occurs is:', numBobs
     


