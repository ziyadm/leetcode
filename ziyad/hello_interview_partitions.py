"""
Problem Statement:

You are given a string 's'. Your task is to partition 's' in such a way that every substring of the partition is a palindrome. Return all possible palindrome partitioning of 's'.

The function will take a string as input and return a list of lists of strings.

Input:
s: A string

Output:
A list of lists of strings, each list representing a possible palindrome partitioning.

Example:

Input: "abc"
Output: [["a", "b", "c"]]

Input: "aaa"
Output: [["a", "a", "a"], ["aa", "a"], ["a", "aa"], ["aaa"]]

Note:
1. s consists of lowercase English letters.
2. 1 <= s.length <= 16.
3. If s is empty, return an empty list.

"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        all_partitions = set()

        def generate_partitions(remaining: str, partitions: List[str]):
            if remaining == "":
                all_partitions.add(tuple(partitions))
                return

            last_string_in_partition = partitions[-1] if len(partitions) > 0 else ""

            if last_string_in_partition + remaining[0] == remaining[0] + last_string_in_partition[::-1]:
                previous_partitions = partitions.copy()

                if len(previous_partitions) == 0:
                    previous_partitions = [last_string_in_partition + remaining[0]]
                else:
                    previous_partitions[-1] = last_string_in_partition + remaining[0]

                generate_partitions(remaining=remaining[1:], partitions=previous_partitions)

            new_partition = partitions.copy()
            new_partition.append(remaining[0])
            generate_partitions(remaining=remaining[1:], partitions=new_partition)

        generate_partitions(remaining=s, partitions=[])

        return [list(partition) for partition in all_partitions]


solution = Solution()
assert solution.partition("abc") == [["a", "b", "c"]]
print(solution.partition("aaa"))
print(solution.partition("aab"))