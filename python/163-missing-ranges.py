from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> \
            List[List[int]]:
        if not nums:
            return [[lower, upper]]

        ranges = []

        for n in nums:
            if n != lower:
                ranges.append([lower, n - 1])
            lower = n + 1

        if lower <= upper:
            ranges.append([lower, upper])

        return ranges
