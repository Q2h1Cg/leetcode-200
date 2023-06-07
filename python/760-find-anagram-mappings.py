class Solution:
    def anagramMappings(self, nums1: list[int], nums2: list[int]) -> list[int]:
        table = {n: i for i, n in enumerate(nums2)}
        return [table[n] for n in nums1]
