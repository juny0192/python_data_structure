def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowel = 'aeiou'
    lower_p = phrase.lower()
    
    vowel_d = {}

    for char_v in vowel:
        if char_v in lower_p:
            count = lower_p.count(char_v)
            vowel_d[char_v] = count
    
    return vowel_d
            
