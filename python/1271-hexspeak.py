class Solution:
    def toHexspeak(self, num: str) -> str:
        tbl = ['O', 'I', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
               'D', 'E', 'F']
        num = int(num)
        ans = ''
        while num != 0:
            num, m = divmod(num, 16)
            if 1 < m < 10:
                return 'ERROR'

            ans = tbl[m] + ans

        return ans
