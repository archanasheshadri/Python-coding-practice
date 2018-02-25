'''
Write a Python function that returns the sublist of strings in aList that contain fewer than 4 characters.
For example, if aList = ["apple", "cat", "dog", "banana"], your function should return: ["cat", "dog"]

This function takes in a list of strings and returns a list of strings. Your function should not modify aList.
'''

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    actualaList = aList[:]
    result = []
    for i in range(len(aList)):
        count = 0
        for letter in aList[i]:
            count += 1
        if count < 4:
            result.append(aList[i])
    return result
        
            
        
    
