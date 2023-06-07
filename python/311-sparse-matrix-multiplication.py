class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[
        List[int]]:
        a1 = self._get_no_zero(mat1)
        a2 = self._get_no_zero(mat2)
        ans = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
        for i1, j1, v1 in a1:
            for i2, j2, v2 in a2:
                if j1 == i2:
                    ans[i1][j2] += v1 * v2

        return ans

    @staticmethod
    def _get_no_zero(m):
        a = []
        for i, row in enumerate(m):
            for j, n in enumerate(row):
                if n != 0:
                    a.append([i, j, n])

        return a
