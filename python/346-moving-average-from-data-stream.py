import collections


class MovingAverage:
    def __init__(self, size: int):
        self._size = size
        self._nums = collections.deque()
        self._sum = 0

    def next(self, val: int) -> float:
        if len(self._nums) == self._size:
            self._sum -= self._nums.popleft()

        self._nums.append(val)
        self._sum += val

        return self._sum / len(self._nums)
