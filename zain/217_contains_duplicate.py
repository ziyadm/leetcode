class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numberSet = set()
        for num in nums:
            if num in numberSet:
                return True
            else:
                numberSet.add(num)
        return False
