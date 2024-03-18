from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_to_anagrams = defaultdict(list)        

        for unsorted in strs:
            sorted_word_to_anagrams["".join(sorted(unsorted))].append(unsorted)

        return [anagram_group for anagram_group in sorted_word_to_anagrams.values()]
        
       
