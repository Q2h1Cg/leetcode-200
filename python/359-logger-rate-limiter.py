class Logger:
    def __init__(self):
        self._printed: dict[str, int] = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self._printed.get(message, -11) + 10 > timestamp:
            return False

        self._printed[message] = timestamp
        return True
