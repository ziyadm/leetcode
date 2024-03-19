from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        
        num_to_frequency = [(key, value) for key, value in frequencies.items()]
        num_to_frequency.sort(key = lambda num_to_frequency: num_to_frequency[1], reverse=True)
        
        return [num for num, frequency in num_to_frequency[0:k]]





