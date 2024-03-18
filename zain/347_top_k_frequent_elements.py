class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        frequencies = {}
        count = 0
        while count <= len(nums):
            frequencies[count] = []
            count += 1
        
        sorted_nums = sorted(nums)
        left = 0
        right = 1
        current_count = 1

        while right <= len(nums):
            if right == len(nums):
                frequencies[current_count].append(nums[left])
                break

            elif nums[right] == nums[left]:
                current_count += 1
                right += 1
                
            else:
                frequencies[current_count].append(nums[left])
                left = right
                right = left + 1
                current_count = 1

        results = []
        for frequency in range(len(nums), 0, -1):
            if frequency in frequencies:
                for number in frequencies[frequency]:
                    results.append(number)
                    if len(results) == k:
                        return results
        return results



