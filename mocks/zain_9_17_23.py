# 09/17 Interview 

# Given an array and an integer k, return an array where4 each element is the maximum element in a subarray of size k

# Empty array -> return empty array
# Can have duplicates in output
# 1 <= K <= size(input)
# Example: input: [10, 18, 22, 3, 5], k = 2 Output: [18, 22, 22, 5]

# Big idea: Use a sliding window of size k, starting from the left most position of input list,
# slide the window over each position, determining the maximum value at each iteration

# For each iteration, we will keep track of max value, may be able to optimize this later
# Time: Iterate over input array: O(n), for each iteration over the input array, we will then
# iterate over the subarray, O(k), and while iterating over the subarray we will do O(1) comparisons to the max value

# O(n*k)

# Storing max value, also storing output list, O(n) complexity

# Idea 2: Iterate over the input array, at each iteration add our new value to a max heap
        # and remove the value that has left the window
# Time: Iterate over the input array: O(n), building the heap once: O(k), subsequent insertions
        # and removals will be O(log(k)). We can say for the first iteration we have O(1)*O(k).0
        # For the second iteration we have O(n-1)*O(2log(k)).
        # Final complexity: O((n)*log(k))
# Space: Store heap of size k, and we will, have to store an output list of size n - 1, 
    # Final complexity: O(n)




# Test cases:
test_1_list = [10, 18, 22, 3, 5]
test_1_k = 2
test_1_output = [18, 22, 22, 5]

test_2_list = [30, 18, 22, 3, 5]
test_2_k = 2
test_2_output = [30, 22, 22, 5]

# Solution

def find_max_of_subarrays(input_list: List[int], k: intß) -> List[int]:
    left = 0
    right = left + k - 1
    first_values = [] 
    output = []
    for i in range(left, right):
        first_values.append(input_list[i])
    sliding_window = max_heap(first_values)
    # For first subarray, return value before iterating
    output.append(sliding_window.max_value())
    current = k 
    while k < len(input_list):
        sliding_window.remove(input_list(left))
        sliding_window.insert(input_list(current))
        output.append(sliding_window.max_value())
    return output





# class max_heap: 

# def max_heap(subarray: List[int]):
    # Create max_heap given an input list of integers
# def insert(value: int):
    # Add the value to the heap, and heapify
# def remove(value: int):
    # Remove the value from the heap, and heapify
# def max_value():
    # Return the maximum value from the heap


