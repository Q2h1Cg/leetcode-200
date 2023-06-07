import math


class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = int(math.log10(n)) + 1
        s = 0
        q = n
        while q != 0:
            q, m = divmod(q, 10)
            s += m ** k

        return s == n
