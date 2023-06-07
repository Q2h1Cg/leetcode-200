import itertools


class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self._zip = itertools.zip_longest(v1, v2)
        self._cur = []
        self._i = 0

    def next(self) -> int:
        if self._i == len(self._cur):
            self._next()

        i = self._i
        self._i += 1
        return self._cur[i]

    def hasNext(self) -> bool:
        if self._i < len(self._cur):
            return True

        try:
            self._next()
        except StopIteration:
            return False

        return True

    def _next(self):
        self._cur = [n for n in next(self._zip) if n is not None]
        self._i = 0
