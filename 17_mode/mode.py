def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    for num1 in nums:
        num1_count = nums.count(num1) 
        for num2 in nums:
            num2_count = nums.count(num2)
            if num1_count > num2_count:
                return num1
