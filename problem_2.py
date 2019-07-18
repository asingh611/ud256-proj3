def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array
    Provided assumption: no repeating number

    Args:
       input_list(list): Input array to search
       number(int): Target of search
    Returns:
       int: Index or -1
    """

    # Return -1 for the case where input list is empty
    if len(input_list) == 0:
        return -1

    offset = 0
    search_list = input_list
    while len(search_list) > 2:
        mid = len(search_list)//2
        if search_list[mid] == number:
            return mid + offset

        # Check range of first half
        left_start_value = search_list[0]
        left_end_value = search_list[mid-1]

        # Check range of second half
        right_start_value = search_list[mid+1]
        right_end_value = search_list[-1]

        # Can check if any of the start or end values are equal to the number being searched?
        if left_start_value == number:
            return 0 + offset
        elif left_end_value == number:
            return mid - 1 + offset
        elif right_start_value == number:
            return mid + 1 + offset
        elif right_end_value == number:
            return len(search_list) - 1 + offset

        # If the rotation is within the left half (the start value is higher than the end value of this half)
        if left_start_value > left_end_value and (number >= left_start_value or number <= left_end_value):
            search_list = search_list[0:mid]
        # Otherwise, the left half is in linear order - does the number fall into that?
        elif left_start_value < left_end_value and left_start_value <= number <= left_end_value:
            search_list = search_list[0:mid]

        # If the rotation is within the right half (the start value is higher than the end value of this half)
        elif right_start_value > right_end_value and (number >= right_start_value or number <= right_end_value):
            search_list = search_list[mid:-1]
            offset += mid
        # Otherwise the right half is in linear order - does the number fall into that?
        elif right_start_value < right_end_value and right_start_value <= number <= right_end_value:
            search_list = search_list[mid:-1]
            offset += mid

        # If the number does not fit into any range
        else:
            return -1

    # Search remaining elements (should be up to 2 remaining)
    if search_list[0] == number:
        return offset
    elif search_list[-1] == number:
        return offset + len(search_list) - 1

    # Otherwise number not found
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# Case 0: Short list
test_function([[2], 2])
# Case 1: Number found (is first number)
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Case 2: Number found (is middle number)
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 10])
# Case 3: Number not found
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 20])
# Case 4: Number in left half
test_function([[8, 10, 1, 2, 3, 4, 5, 6, 7], 10])
# Case 5: Number in right half
test_function([[3, 4, 5, 6, 7, 8, 10, 1, 2], 10])
# Case 6: Empty list
test_function([[], 10])
# Case 7: Number found (is last number)
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 4])

# test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# test_function([[6, 7, 8, 1, 2, 3, 4], 1])
# test_function([[6, 7, 8, 1, 2, 3, 4], 10])
