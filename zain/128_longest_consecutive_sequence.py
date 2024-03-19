class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        max_length = 0

        for num in nums:
            if num - 1 not in number_set: 
                current_length = 1
                next_num = num + 1
                
                while next_num in number_set:
                    current_length += 1
                    next_num += 1
                
                max_length = max(current_length, max_length)
                if max_length >= len(nums) / 2:
                    return max_length
        
        return max_length
