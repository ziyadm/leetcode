class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running_product = 1
        output = [None]*len(nums)
        for i in range(len(nums)):
            output[i] = running_product
            running_product *= nums[i]
            
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output


   


