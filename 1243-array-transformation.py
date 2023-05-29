class Solution:
    def transformArray(self, arr: list[int]) -> list[int]:
        if len(arr) < 3:
            return arr

        prev = None
        while arr != prev:
            prev = arr.copy()

            for i, n in enumerate(arr[1:-1], 1):
                if n < prev[i - 1] and n < prev[i + 1]:
                    arr[i] = n + 1
                elif n > prev[i - 1] and n > prev[i + 1]:
                    arr[i] = n - 1

        return arr
