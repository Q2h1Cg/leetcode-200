class Solution:
    def missingNumber(self, arr: list[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)
        expect = arr[0] + diff
        for n in arr[1:]:
            if n != expect:
                return expect

            expect += diff

        return arr[0]
