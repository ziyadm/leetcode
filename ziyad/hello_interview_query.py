"""
Problem Statement:

You are given a list of valid words and an input string that may include wildcard characters (?). Your task is to determine whether the input string can be a valid word from the list. A wildcard character (?) can match any single character.

The function will take a list of words as the dictionary and a query string. It will return a boolean value indicating whether the query can match any word in the dictionary.

Input:
- A list of strings dictionary (1 <= |dictionary| <= 5000), where each string has a length of 1 to 15 and consists of lowercase alphabets.
- A string query (1 <= |query| <= 15) consisting of lowercase alphabets and possibly the wildcard character (?).

Output:
- A boolean value: True if the query can match any word in the dictionary, and False otherwise.

If there are multiple words in the dictionary that match the query, it is still considered valid.

Example:

Input: dictionary = ["cat", "bat", "rat", "drat"], query = "c?t"
Output: True

Note:
- The wildcard character (?) can represent any single character.
- Your solution is not allowed to use regular expressions.

"""


from typing import List 
from collections import defaultdict

class Solution:
    def is_valid_word(self, dictionary: List[str], query: str) -> bool:
        char_at_index_to_words = defaultdict(list)

        for word in dictionary:
            for index, char in enumerate(word):
                char_at_index_to_words[(char, index)].append(word)
                char_at_index_to_words[('?', index)].append(word)

        for index, letter in enumerate(query):
            if index == 0:
                matching_words = set(char_at_index_to_words[(letter, index)])
            matching_words &= set(char_at_index_to_words[(letter, index)])

        return len(matching_words) > 0

solution = Solution()
assert solution.is_valid_word(
    dictionary = ["cat", "bat", "rat", "drat"], query = "c?t")
assert solution.is_valid_word(
    dictionary = ["cat", "bat", "rat", "drat"], query = "cat")
assert solution.is_valid_word(
    dictionary = ["cat", "bat", "rat", "drat"], query = "???")
assert not solution.is_valid_word(
    dictionary = ["cat", "bat", "rat", "drat"], query = "cut")
assert not solution.is_valid_word(
    dictionary = [], query = "cut")
assert not solution.is_valid_word(
    dictionary = ["cat", "bat", "rat", "drat"], query = "drats")

