import heapq
from math import floor


class Solution:
    def minStoneSum(self, piles, k):
        heap = []
        for item in piles:
            heapq.heappush(heap, -item)

        for _ in range(k):
            minus_value = heapq.heappop(heap)
            max_value = minus_value * -1
            item = max_value - floor(max_value / 2)
            heapq.heappush(heap, -item)

        return sum([-val for val in heap])
        '''
        for _ in range(k):
            max_value = max(piles)
            idx = piles.index(max_value)
            value = max_value - floor(max_value/2)
            # print(value)
            piles[idx] = value

        return sum(piles)
        '''


a = Solution()
print(a.minStoneSum([5, 4, 9], 2))