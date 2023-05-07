class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2
            if arr[mid] >= mid:
                high = mid - 1
            else:
                low = mid + 1

        return low if len(arr) > low == arr[low] else -1
