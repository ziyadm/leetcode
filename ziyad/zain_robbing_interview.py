"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing
each of them is that adjacent houses have security systems connected and it will automatically
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4

Input: nums = [2,7,9,3,1]
Output: 12
"""

"""
Approach:
- generate all valid sets of indexes, where no two adjacent indexes are picked (recurisvely)
- maximize money across all sets generated
- optimize via memoization
- possible to implement iteratively instead of recursively
"""
from typing import List

def maximum_robbery(money_per_house: List[int]) -> int:
    if len(money_per_house) == 1:
        return money_per_house[0]
    elif len(money_per_house) == 2:
        return max(money_per_house[0], money_per_house[1])
    elif len(money_per_house) == 3:
        return max(money_per_house[0] + money_per_house[2], money_per_house[1])
    else:
        # option 1: steal from first house
        steal_from_first = money_per_house[0] + maximum_robbery(money_per_house[2:])
        # option 2: do not steal from first house
        donot_steal_from_first = maximum_robbery(money_per_house[1:])
        return max(steal_from_first, donot_steal_from_first)

assert maximum_robbery(money_per_house = [1,2,3,1]) == 4
assert maximum_robbery(money_per_house = [2,7,9,3,1,3,4,5,6,7,4,8,6,9,11]) == 45