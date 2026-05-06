from heapq import *
class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        top_max = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, -top_max)

        if len(self.min_heap) > len(self.max_heap):
            top_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -top_min)

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
            
        return (self.min_heap[0] - self.max_heap[0]) / 2