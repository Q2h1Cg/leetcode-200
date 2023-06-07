from typing import List


class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str,
                         word2: str) -> int:
        shortest = len(wordsDict)
        pos1 = pos2 = -shortest

        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
                distance = i - pos2
            elif word == word2:
                pos2 = i
                distance = i - pos1
            else:
                continue

            shortest = min(shortest, distance)

        return shortest
