import collections


class TwoSum:
    counter: collections.Counter[int]

    def __init__(self):
        self.counter = collections.Counter()

    def add(self, number: int) -> None:
        self.counter[number] += 1

    def find(self, value: int) -> bool:
        for n in self.counter:
            other = value - n
            if other in self.counter and (other != n or self.counter[n] >= 2):
                return True

        return False
