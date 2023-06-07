class Solution:
    def _reverse(self, s: list[str], begin, end):
        while begin < end:
            s[begin], s[end] = s[end], s[begin]
            begin += 1
            end -= 1

    def reverseWords(self, s: List[str]) -> None:
        self._reverse(s, 0, len(s) - 1)

        begin = 0
        for i in range(len(s)):
            if s[i] == ' ':
                self._reverse(s, begin, i - 1)
                begin = i + 1

        self._reverse(s, begin, len(s) - 1)
