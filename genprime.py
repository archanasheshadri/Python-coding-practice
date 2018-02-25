def genPrimes():
    p = []
    yield 2
    p.append(2)
    num = 2
    
    while True:
        num += 1
        for prime in p :
            if (num%prime) == 0:
                break
        else:
            yield num
            p.append(num)

                
        
        
    
    
