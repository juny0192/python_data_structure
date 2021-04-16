def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    lower_p = phrase.lower()
    result = ''

    for ele in lower_p.split(' '):
        cap_ele = ele.capitalize()
        joined_ele = "".join(cap_ele)
        result += joined_ele + ' '
        
    return result
