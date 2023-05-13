class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        table = [0] * 1001
        for num in nums:
            table[num] += 1

        for i in range(1000, -1, -1):
            if table[i] == 1:
                return i

        return -1
