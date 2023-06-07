import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = collections.Counter(s)
        single = 0
        for n in counter.values():
            if n % 2 == 0:
                continue

            single += 1

            if single > 1:
                return False

        return True
