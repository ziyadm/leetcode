class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0]*len(temperatures)
        stack = []
        index = 0

        for index, value in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < value:
                results[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)

        return results
