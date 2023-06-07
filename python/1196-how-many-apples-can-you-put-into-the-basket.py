class Solution:
    def maxNumberOfApples(self, weight: list[int]) -> int:
        weight.sort()

        n = 0
        for i, w in enumerate(weight):
            n += w
            if n > 5000:
                return i

        return len(weight)
