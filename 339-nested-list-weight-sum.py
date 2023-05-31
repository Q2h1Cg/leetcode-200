class Solution:
    def _depth_sum(self, depth, nested):
        s = 0

        for ni in nested:
            if ni.isInteger():
                s += depth * ni.getInteger()
            else:
                s += self._depth_sum(depth + 1, ni.getList())

        return s

    def depthSum(self, nestedList: list[NestedInteger]) -> int:
        return self._depth_sum(1, nestedList)
