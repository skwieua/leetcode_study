import heapq


class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        cnt = 0
        heap_list = [capacity[i] - rocks[i] for i in range(len(capacity))]

        heapq.heapify(heap_list)
        while heap_list:
            if additionalRocks <= 0:
                break

            min_value = heapq.heappop(heap_list)
            if min_value == 0:
                cnt += 1
                continue
            else:
                if additionalRocks >= min_value:
                    additionalRocks -= min_value
                    cnt += 1
                else:
                    break

        return cnt