class Solution:
    def sumOfDigits(self, nums: list[int]) -> int:
        n = min(nums)
        s = 0
        while n != 0:
            n, m = divmod(n, 10)
            s += m

        return 0 if s % 2 == 1 else 1
