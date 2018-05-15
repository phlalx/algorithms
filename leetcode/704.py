#TAGS kth element, heap
# classic

import heapq

def insert(heap, v, k):
    if len(heap) < k or v > heap[0]:
        heapq.heappush(heap, v)
    if len(heap) > k:
        heapq.heappop(heap)

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._heap = []
        self._k = k
        for v in nums:
            insert(self._heap, v, k)
        

    def add(self, val: int) -> int:
        insert(self._heap, val, self._k)
        return self._heap[0]



