class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        begin = 0
        states = []

        while (begin := currentState.find('++', begin)) != -1:
            states.append(
                currentState[:begin] + '--' + currentState[begin + 2:])
            begin += 1

        return states
