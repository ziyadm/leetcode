"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products_from_left = [1] * len(nums)
        products_from_right = [1] * len(nums)
        products_except_self = [1] * len(nums)

        product_from_left = 1
        product_from_right = 1
        for index in range(len(nums)):
            product_from_left *= nums[index]
            product_from_right *= nums[len(nums) - index - 1]

            products_from_left[index] = product_from_left
            products_from_right[len(nums) - index - 1] = product_from_right

        for index in range(len(nums)):
            left_product = 1 if index == 0 else products_from_left[index - 1]
            right_product = 1 if index == len(nums) - 1 else products_from_right[index + 1]

            products_except_self[index] = left_product * right_product 

        return products_except_self

# Tests
solution = Solution()
assert solution.productExceptSelf(nums = [1,2,3,4]) == [24,12,8,6]
assert solution.productExceptSelf(nums = [-1,1,0,-3,3]) == [0,0,9,0,0]