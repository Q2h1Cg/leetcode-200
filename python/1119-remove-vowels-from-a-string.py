class Solution:
    def removeVowels(self, s: str) -> str:
        tbl = str.maketrans('', '', 'aeiou')
        return s.translate(tbl)
