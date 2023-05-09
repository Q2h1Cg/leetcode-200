class Solution:
    def indexPairs(self, text: str, words: list[str]) -> list[list[int]]:
        words = set(words)
        lens = set(len(word) for word in words)
        ret = []
        for i in range(len(text)):
            for len_ in lens:
                j = i + len_
                if j <= len(text) and text[i: j] in words:
                    ret.append([i, j - 1])

        return sorted(ret)
