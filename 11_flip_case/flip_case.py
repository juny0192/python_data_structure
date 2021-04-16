def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    to_swap = to_swap.lower()
    swaped = ""

    for char in phrase:
        if char.lower() == to_swap:
            char = char.swapcase()
        swaped += char

    return swaped

            



            
    #     phrase.replace()
    # if to_swap.islower():
    #     if to_swap in phrase:
    #         phrase.replace(to_swap, to_swap.upper())
    #     if to_swap.upper() in phrase:

    #     print(phrase.replace(to_swap.upper(), to_swap.lower()))
        

    # if to_swap.isupper():
    #     phrase.replace(to_swap, to_swap.lower())
    #     phrase.replace(to_swap.lower(), to_swap.upper())
    #     return phrase
        

print(flip_case('Aaaahhh', 'a'))

