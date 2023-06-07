class Solution:
    def confusingNumber(self, n: int) -> bool:
        tbl = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        d = n
        new = 0
        while d != 0:
            d, m = divmod(d, 10)
            if m not in tbl:
                return False

            new = new * 10 + tbl[m]

        return new != n
