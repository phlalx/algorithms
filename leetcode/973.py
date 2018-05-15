#TAGS heap, k closest

# N * log(N - K) min heap

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        res = []
        heap = []  # keep the N - K further points to origin
        for x, y in points:
            d = x ** 2 + y ** 2
            heapq.heappush(heap, (d, x, y))
            if len(heap) == n - K + 1:
                _, x, y = heapq.heappop(heap)
                res.append((x, y))
        return res
           
# N * log(K) max heap

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        heap = []  # keep the K closest points to origin, max heap
        for x, y in points:
            d = x ** 2 + y ** 2
            heapq.heappush(heap, (-d, x, y))
            if len(heap) == K + 1:
                heapq.heappop(heap)
        return [(x, y) for _, x, y in heap]

# other solution = O(n) use quick k-select
# disavantage: not online, not stable
#
            
