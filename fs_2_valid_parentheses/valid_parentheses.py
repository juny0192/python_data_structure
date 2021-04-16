def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if len(parens) % 2 == 0:
         
        first_half = parens[0:len(parens)//2]
        second_half = parens[len(parens)//2 if len(parens)%2 == 0 else ((len(parens)//2)+1):]

        if first_half[0] == '(' and second_half[-1] == ')':
            return True

        return False

    return False
