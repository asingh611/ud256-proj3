def sqrt(number, initial_guess=10):
    """
    Calculate the floored square root of a number
    If input is negative, return number to multiply by i

    Args:
       number(int): Number to find the floored squared root
       initial_guess(int): Starting guess for square root
    Returns:
       int: Floored Square Root
    """

    # If input number is negative, flip the sign (will return number to be multiplied by i)
    if number < 0:
        number = number * -1

    # If you are taking the square root of 0, it would be 0
    if number == 0:
        return 0

    current_guess = initial_guess

    lower_bound = 0  # Lowest real value possible
    upper_bound = initial_guess  # Use initial guess as the original upper bound for the guess range

    # Shift the bounds of the guess range based on the (upper bound)^2 relative to the input number
    while upper_bound * upper_bound < number:
        lower_bound = upper_bound
        upper_bound = upper_bound * 2

    # If you got the guess right on the first try
    if upper_bound * upper_bound == number:
        return initial_guess

    # Otherwise we need to iterate between the lower and the upper bound
    while abs(current_guess - (upper_bound + lower_bound)//2) > 0:
        # Find the middle of the range
        midpoint = (upper_bound + lower_bound)//2

        # Maybe the midpoint was the answer?
        if midpoint * midpoint == number:
            return midpoint

        # Otherwise adjust the range appropriately based on the value of (midpoint)^2 relative to the bounds
        elif midpoint * midpoint > number:
            upper_bound = midpoint
        else:
            lower_bound = midpoint

        current_guess = midpoint

    return current_guess


print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (9 == sqrt(90)) else "Fail")
print("Pass" if (6 == sqrt(40)) else "Fail")
print("Pass" if (11 == sqrt(140)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(-27)) else "Fail")
