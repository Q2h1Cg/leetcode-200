import collections


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        table = collections.defaultdict(lambda: '',
                                        {
                                            '0': '0',
                                            '1': '1',
                                            '8': '8',
                                            '6': '9',
                                            '9': '6',
                                        })

        i, j = 0, len(num) - 1
        while i <= j:
            if num[j] != table[num[i]]:
                return False

            i += 1
            j -= 1

        return True
