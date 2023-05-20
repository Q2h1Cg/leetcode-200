import bisect


class Solution:
    def arraysIntersection(self, arr1: list[int], arr2: list[int],
                           arr3: list[int]) -> list[int]:
        mi = max(arr1[0], arr2[0], arr3[0])
        i_beg = bisect.bisect_left(arr1, mi)
        j_beg = bisect.bisect_left(arr2, mi)
        k_beg = bisect.bisect_left(arr3, mi)

        ma = min(arr1[-1], arr2[-1], arr3[-1])
        i_end = bisect.bisect_right(arr1, ma, i_beg)
        j_end = bisect.bisect_right(arr2, ma, j_beg)
        k_end = bisect.bisect_right(arr3, ma, k_beg)

        ans = []
        while i_beg < i_end and j_beg < j_end and k_beg < k_end:
            x, y, z = arr1[i_beg], arr2[j_beg], arr3[k_beg]

            if x == y == z:
                ans.append(x)
                i_beg += 1
                j_beg += 1
                k_beg += 1
            elif x <= y and x <= z:
                i_beg += 1
            elif y <= x and y <= z:
                j_beg += 1
            else:
                k_beg += 1

        return ans
