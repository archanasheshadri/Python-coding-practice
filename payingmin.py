# Author: Archana Sheshadri

#balance = 4842
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

#remainingBalance = balance
#totalPaid = 0

#for month in range(1,13):
#    minimumPayment = round(remainingBalance * monthlyPaymentRate, 2)
#    unpaidBalance = remainingBalance - minimumPayment
    
#    interest = annualInterestRate/12.0 * unpaidBalance
#    remainingBalance = round(unpaidBalance + interest, 2)
#    totalPaid += minimumPayment 
#    print 'Month: ' + str(month)
#    print 'Minimum monthly payment: ' + str(minimumPayment)
#    print 'Remaining balance: ' + str(remainingBalance)

#print 'Total paid: ' + str(totalPaid)
#print 'Remaining balance: ' + str(remainingBalance)

    
    
#Paying debt in a year
#Start with $10 payments per month and calculate whether the balance will be paid off in a year this way (be sure to take into account the interest accrued each month).
#If $10 monthly payments are insufficient to pay off the debt within a year, increase the monthly payment by $10 and repeat.
balance = 3926
annualInterestRate = 0.2

def minMonthlyPayment(balance, annualInterestRate, minMonPayment):
    '''
    balance: integer variable
    annualInterestRate: float variable

    returns: minimum monthly payment
    '''
    updatedBalance = balance
    for month in range(1,13):
        interest = annualInterestRate/12.0
        monthlyUnpaidBalance = updatedBalance - minMonPayment
        updatedBalance = monthlyUnpaidBalance + interest * monthlyUnpaidBalance
    return updatedBalance
    

    
minMonPayment = 10
updatedBalance = minMonthlyPayment(balance, annualInterestRate, minMonPayment)

while True:
    if updatedBalance <= 0:
        print 'Lowest Payment: ' + str(minMonPayment)
        break
    else:
        minMonPayment += 10
        updatedBalance = minMonthlyPayment(balance, annualInterestRate, minMonPayment)
    




