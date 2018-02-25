def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    result = []
    if aDict.keys() != []:
        values = aDict.values()
        uniqueValue = []
        values.sort()
        temp = values[0]
        count = 0
        for value in values[1:]:
            if temp == value:
                if value in uniqueValue:
                    uniqueValue.remove(value)
                count += 1
            else:
                if count == 0:
                    uniqueValue.append(temp)
                uniqueValue.append(value)
                count += 1
                temp = value
        
        if len(values) == 1:
            uniqueValue.append(temp)
            
        for key in aDict.keys():        
            if aDict[key] in uniqueValue:
                result.append(key)
        result.sort()
    return result
            
