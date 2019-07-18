import random


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    # If empty list provided, return None
    if len(ints) == 0:
        return None, None

    # If there is only one number in the list, then the min and max are the same
    if len(ints) == 1:
        return ints[0], ints[0]

    # Initialize the minimum and maximum as the first element of the list
    smallest = ints[0]
    largest = ints[0]

    # Scan through each element in the array
    for number in ints:
        # Check if number is smaller than the smallest recorded so far
        if number < smallest:
            smallest = number
        # Check if number is larger than the largest recorded so far
        if number > largest:
            largest = number

    return smallest, largest


# Test cases
# Case 1: List of random numbers (ranging from -5 to 9)
rand_list = [i for i in range(-5, 10)]
random.shuffle(rand_list)
print("Pass" if ((-5, 9) == get_min_max(rand_list)) else "Fail")

# Case 2: Empty list
print("Pass" if ((None, None) == get_min_max([])) else "Fail")

# Case 3: List with one item
print("Pass" if ((2, 2) == get_min_max([2])) else "Fail")

# Case 4: List multiple same values
print("Pass" if ((2, 2) == get_min_max([2, 2, 2, 2])) else "Fail")
