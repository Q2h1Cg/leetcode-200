class Solution:
    def twoSumLessThanK(self, nums: list[int], k: int) -> int:
        nums.sort()

        ss = -1
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s < k:
                ss = max(ss, s)
                i += 1
            else:
                j -= 1

        return ss
