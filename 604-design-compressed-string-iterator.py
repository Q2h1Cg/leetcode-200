class StringIterator:
    def __init__(self, compressedString: str):
        self._str = compressedString
        self._size = len(compressedString)
        self._pos = 0
        self._num = 0
        self._char = None

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        if self._num == 0:
            self._char = self._str[self._pos]
            self._pos += 1

            while self._pos < self._size \
                    and (c := self._str[self._pos]).isdigit():
                self._num = self._num * 10 + int(c)
                self._pos += 1

        self._num -= 1
        return self._char

    def hasNext(self) -> bool:
        return self._pos < self._size or self._num != 0
