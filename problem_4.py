def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # Expected time complexity -> O(n)
    # Since there are only 3 possibilities for values, create 3 arrays to hold each type of digit
    zeros = []
    ones = []
    twos = []

    # Linearly traverse list and organize numbers into appropriate list
    for number in input_list:
        if number == 0:
            zeros.append(0)
        elif number == 1:
            ones.append(1)
        else:
            twos.append(2)

    # Concatenate the 3 lists into final result
    return zeros + ones + twos


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])