# Would need implementation of sorting algorithm
# Requirement: O(nlog(n)) efficiency -> use MergeSort or QuickSort


def mergesort(items):
    # Base case, a list of 0 or 1 items is already sorted
    if len(items) <= 1:
        return items

    # Otherwise, find the midpoint and split the list
    mid = len(items)//2
    left = items[0:mid]
    right = items[mid:]

    # Call mergesort recursively with the left and right half
    left = mergesort(left)
    right = mergesort(right)

    # Merge our two halves and return
    return merge(left, right)


def merge(left, right):
    # Given two ordered lists, merge them together in order,
    # returning the merged list.
    merged = []
    left_index = 0
    right_index = 0

    # Iterate through the ordered lists until you reach the end of one list
    # Modification to the code compared to the example - numbers to be sorted in descending order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    # Add the remaining values from either the left or right list
    merged += left[left_index:]
    merged += right[right_index:]

    return merged


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    # If the input list doesn't contain anything, return empty array
    if len(input_list) == 0:
        return []

    # If the input list has one number, then the max sum is that number and zero
    if len(input_list) == 1:
        return [input_list[0], 0]

    # Get the ordered list via merge sort
    ordered_list = mergesort(input_list)

    # Get every other number in the sorted list
    left_number_array = ordered_list[0::2]
    right_number_array = ordered_list[1::2]

    # Build the return values
    left_number_string = ''
    for number in left_number_array:
        left_number_string += str(number)

    right_number_string = ''
    for number in right_number_array:
        right_number_string += str(number)

    return [int(left_number_string), int(right_number_string)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases

test_function([[1, 2, 3, 4, 5], [542, 31]])

test_function([[4, 6, 2, 5, 9, 8], [964, 852]])

test_function([[1, 4], [4, 1]])

test_function([[1, 4, 2], [41, 2]])

# Edge Case 1: No inputs
test_function([[], []])

# Edge Case 2: 1 number input
test_function([[1], [1, 0]])
