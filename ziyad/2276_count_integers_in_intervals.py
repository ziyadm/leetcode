"""
Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.

 

Example 1:

Input
["CountIntervals", "add", "add", "count", "add", "count"]
[[], [2, 3], [7, 10], [], [5, 8], []]
Output
[null, null, null, 6, null, 8]

Explanation
CountIntervals countIntervals = new CountIntervals(); // initialize the object with an empty set of intervals. 
countIntervals.add(2, 3);  // add [2, 3] to the set of intervals.
countIntervals.add(7, 10); // add [7, 10] to the set of intervals.
countIntervals.count();    // return 6
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 7, 8, 9, and 10 are present in the interval [7, 10].
countIntervals.add(5, 8);  // add [5, 8] to the set of intervals.
countIntervals.count();    // return 8
                           // the integers 2 and 3 are present in the interval [2, 3].
                           // the integers 5 and 6 are present in the interval [5, 8].
                           // the integers 7 and 8 are present in the intervals [5, 8] and [7, 10].
                           // the integers 9 and 10 are present in the interval [7, 10].
"""
import unittest

class CountIntervals:

    def __init__(self):
        self.timestamps = []

    def add(self, left: int, right: int) -> None:
        self.timestamps.append((left, 's'))
        self.timestamps.append((right, 'e'))
        self.timestamps.sort(key=lambda timestamp: timestamp[1], reverse=True)
        self.timestamps.sort(key=lambda timestamp: timestamp[0])

    def count(self) -> int:
        currently_open_intervals = 0
        current_interval_start = 0
        current_interval_end = 0
        integers_present = 0

        for timestamp in self.timestamps:
            if timestamp[1] == 's':
                currently_open_intervals += 1
                if currently_open_intervals == 1:
                    current_interval_start = timestamp[0]
            if timestamp[1] == 'e':
                currently_open_intervals -= 1
                if currently_open_intervals == 0:
                    current_interval_end = timestamp[0]
                    integers_present += (current_interval_end - current_interval_start + 1)

        return integers_present


class CountIntervalsTest(unittest.TestCase):
    def setUp(self):
        self.count_intervals = CountIntervals()
        self.count_intervals.add(2,3)
        self.count_intervals.add(7,10)
    
    def test(self):
        self.assertEqual(self.count_intervals.count(), 6)
        self.count_intervals.add(5,8)
        self.assertEqual(self.count_intervals.count(), 8)

if __name__ == '__main__':
    unittest.main()

# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
