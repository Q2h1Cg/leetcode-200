import bisect


class Solution:
    def isMajorityElement(self, nums: list[int], target: int) -> bool:
        pos = bisect.bisect_left(nums, target)
        len_ = len(nums)
        return pos < len_ / 2 and nums[pos + len_ // 2] == target
