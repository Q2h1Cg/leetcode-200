class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        keyboard = dict((c, i) for i, c in enumerate(keyboard))
        s = 0
        prev = 0
        for c in word:
            i = keyboard[c]
            s += abs(i - prev)
            prev = i

        return s
