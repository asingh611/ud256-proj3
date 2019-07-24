# UD256 Project 3
## About this project
This project consist of a series of tasks that are meant review the basic algorithms concepts covered in this unit

## Problem 1

In this problem, the floored square root of a number is found without using the built-in square root function. The expected time complexity is O(log(n)). In order to achieve this, binary search is used. In this case, we are doing a binary search along the number line. The inital lower bound is zero, because there are no negative values for the square root of a number. For the upper bound of the set of integers to perform the binary search on, there is an initial guess parameter that the user can use to give an approximation to the answer (default value is 10). 

Next, the upper bound in increased as needed until the upper bound multiplied by itself is greater than the input number. The overall runtime of the algorithm is affected by how good of an initial guess is made. 

Now that the upper bound is established, bisect the range until the midpoint multiplied by itself is equal to the input number, or there is only one number left, which would be the floored value

## Problem 2

In this problem, the sorted non-repeating search array has a rotation in a random location. The expected run time is O(log(n)). In order to achieve this, some kind of binary search is needed. 

We can still split the range by the midpoint. The start and end numbers of the left and right halves can be inspected to see which range (if either) contains the rotation (checking if the starting number is greater than the ending number of the range). In the range that contains the rotation, the range is valid for numbers greater than the starting number and less than the ending number. This modified binary search is continued in this manner until the number is found or -1 is returned.

## Problem 3

In this problem, the goal is to take in a set of numbers and produce the two numbers from that set of numbers that would have the largest sum. It seems that the maximum sum results from creating two numbers that consist of alternating numbers from the original array starting from the highest to the lowest number. The original input array would need to be sorted. Since the expected run time is O(n*log(n)), Merge Sort or Quick Sort would need to be used. I used Merge Sort in solving this problem, sorting in descending order. With the array sorted, I formed a left number array and a right number array by getting every other number from the sorted array. Then I build the numbers from the array and return them. 

## Problem 4

In this problem, the task is to sort a list of numbers that only contain 0, 1 or 2. The expected runtime is O(n). Since there are only 3 possibliities for values in this list, I created 3 lists to hold the zeros, ones and twos. Then I linearly traversed the original list and assigned the current element to its appropriate storage list based on its value. Once the list is traversed, the 3 storage lists are concatenated, which is also an O(n) operation. 

## Problem 5

In this problem, a trie is used to implement an autocomplete function such that all of the suffixes for a given prefix are returned. A Trie and TrieNode class are given to be implemented. The autocomplete elements reside in TrieNodes within a Trie object. A TrieNode contains a value and children, which are stored in a dictionary such that each entry is [next character, <TrieNode for next character>]. The TrieNode has an insert function, which will insert a provided character into the children dictionary if it doesn't already exist. Since children are stored in a dicionary, insert is O(1). The TrieNode class also contains a suffixes function which recursively gathers all of the suffixes from children nodes. Within each recursion, we need to iterate over each child in the children dictionary, so that is O(n). The Trie class contains an insert function, which calls the insert function of the node for each character being inserted. Although inserting a single character is O(1), since we loop through each character, this is O(n). The find function also loops through each character in the prefix being searched for, so that is also O(n).

## Problem 6

In this problem, the goal is to get the min and max value from an input list in O(n) time, with the additional goal of finding the min and max in a single traversal. In order to do this, the first value of the list is stored as the min and the max. Then the list is linearly traversed and for each number along the list, it is compared against the current min and max value, which are updated as needed. The min and max values are then returned. 

## Problem 7

In this problem, the task is to implement a HTTP router using a Trie. The path segments reside in RouteTrieNodes within a RouteTrie object. The Router class wraps the RouteTrie object and handles the incoming path requests. The RouteTrieNode stores its path and a handler, and stores its children RouteTrieNodes within a dictionary. The insert method adds children to that dictionary in O(1). The RouteTrie has a root node and root node handler, which are initialized when the Router class is initialized. The Router class has a add_handler function that takes in a path, has the path split into a path array by the split_path function and then calls the insert function in the RouteTrie class. The insert function in the RouteTrie class calls the insert function of the RouteTrieNode class. Since I'm looping over each element in the path array, this is O(n). The Router class also contains a lookup fuction, which takes in a path, has the path split by the split_path function and then calls the find function in the RouteTrie class. Since I'm also looping over each element of the path array here, this is also O(n). My code should work for the additional cases of a path not found and a path with a trailing "/".