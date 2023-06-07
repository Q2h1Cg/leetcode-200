import collections
import heapq


class Solution:
    def highFive(self, items: list[list[int]]) -> list[list[int]]:
        table = collections.defaultdict(list)
        for id_, score in items:
            if len(table[id_]) < 5:
                heapq.heappush(table[id_], score)
            else:
                heapq.heappushpop(table[id_], score)

        return [[id_, sum(scores) // 5] for id_, scores in
                sorted(table.items())]
