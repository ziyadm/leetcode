class Solution:
    def groupAnagrams(self, strs):
        sorted_dict = {}
        sorted_set = set()
        

        for original_string in strs:
            sorted_string = "".join(sorted(original_string))
            if sorted_string in sorted_set:
                sorted_dict[sorted_string].append(original_string)
            else:
                sorted_dict[sorted_string] = [original_string]
            sorted_set.add(sorted_string)
       
        results = []

        for sorted_string in sorted_set:
            results.append(sorted_dict[sorted_string])
        return results
        
       
