class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = 0
        i = 0

        for c in abbr:
            if c.isdigit():
                if n == 0 and c == '0':
                    return False

                n = n * 10 + int(c)
            else:
                i += n
                n = 0

                if i >= len(word) or word[i] != c:
                    return False

                i += 1

        return n == len(word) - i
