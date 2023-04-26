class Solution:
    def areSentencesSimilar(self, sentence1: list[str], sentence2: list[str],
                            similarPairs: list[list[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        table = set((w1, w2) for w1, w2 in similarPairs)
        return all(w1 == w2 or (w1, w2) in table or (w2, w1) in table
                   for w1, w2 in zip(sentence1, sentence2))
