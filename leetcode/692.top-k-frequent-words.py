#TAGS heap, easy
#trick! first reflex is to use a max heap, and retrieve the first k elements
#but it's smarter to use a min heap, because we can maintain the size to k
# by comparing the current smaller element in the heap to the next
# elem

from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [ (float('-inf'), None) ]
        for word, freq in count.items():
            if len(heap) < k:
                heappush(heap, (freq, word))
            elif (freq, word) > heap[0]:
                heappop(heap)
                heappush(heap, (freq, word))
        res = []
        for _ in range(k):
            val = heappop(heap)[1]
            res.append(val)
        return res[::-1]

