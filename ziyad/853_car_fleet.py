"""
There are n cars going to the same destination along a one-lane road. The destination is target miles away.
You are given two integer array position and speed,
both of length n, where position[i] is the position of the ith car and speed[i]
is the speed of the ith car (in miles per hour).
A car can never pass another car ahead of it, but it can catch up to it and drive
bumper to bumper at the same speed.
The faster car will slow down to match the slower car's speed.
The distance between these two cars is ignored (i.e., they are assumed to have the same position).
A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.
If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
Return the number of car fleets that will arrive at the destination.

Example 1:
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
The fleet moves at speed 1 until it reaches target.
Note that no other cars meet these fleets before the destination, so the answer is 3.

Example 2:
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation: There is only one car, hence there is only one fleet.

Example 3:
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at speed 2.
Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6.
The fleet moves at speed 1 until it reaches target.
"""

"""
    Ziyad's Notes:
    - calculate the time it will take each car to reach the target
    - if a car at an earlier position can reach the target in less time than a car at a later position, they become one fleet
    - calculate a [(original_position, time_to_reach_target)] array
    - sort by positions, closest to target
    - while theres a car that takes more time to reach the target than a car behind it, merge those into a fleet

"""

from typing import List
import math
import unittest

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 0
        positions_and_speed = sorted(zip(position, speed), key=lambda pos_and_speed: pos_and_speed[0], reverse=True)
        times_to_target = [(target-position)/speed for position, speed in positions_and_speed]

        while times_to_target:
            lead_car_time = times_to_target.pop()
            if len(times_to_target) > 0 and lead_car_time <= times_to_target[-1]:
                times_to_target[-1] = lead_car_time
            else:
                fleets += 1

        return fleets
        

class SolutionTest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_multiple_fleets(self):
        self.assertEquals(self.solution.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]), 3)

    def test_all_fleets_merge(self):
        self.assertEquals(self.solution.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]), 1)

unittest.main()