def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    dic1 = {}
    dic2 = {}
    num1 = str(num1)
    num2 = str(num2)

    for val in num1:       
        count = num1.count(val)
        dic1[val] = count

        for val in num2:
            count = num2.count(val)
            dic2[val] = count
    
    return True if dic1 == dic2 else False
