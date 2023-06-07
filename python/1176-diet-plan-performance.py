class Solution:
    def dietPlanPerformance(self, calories: list[int], k: int, lower: int,
                            upper: int) -> int:
        curr = sum(calories[:k])
        if curr < lower:
            total = -1
        elif curr > upper:
            total = 1
        else:
            total = 0

        for i, c in enumerate(calories[k:], k):
            curr -= calories[i - k]
            curr += c
            if curr < lower:
                total -= 1
            elif curr > upper:
                total += 1

        return total
