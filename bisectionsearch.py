# lecture 3.6, slide 2
# bisection search to guess a number

low = 0
high = 100

print ("Please think of a number between 0 and 100!")
while True:
    ans = (high + low)/2
    print('Is your secret number ' + str(ans))
    print 'Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.',
    x = str(raw_input())
   
    if x == 'h':
        high = ans
    elif x == 'l':
        low = ans
    elif x =='c':
        print ('Game over. Your secret number was:' + str(ans))
        break
    else:
        print ('Sorry, I did not understand your input.')
        
    
        
        
