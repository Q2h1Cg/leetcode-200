class Solution:
    def countLetters(self, s: str) -> int:
        total = 0
        p = 0
        i = 0
        for i, c in enumerate(s):
            if c != s[p]:
                n = i - p
                total += (n + 1) / 2 * n
                p = i

        n = i + 1 - p
        total += (n + 1) / 2 * n

        return int(total)
