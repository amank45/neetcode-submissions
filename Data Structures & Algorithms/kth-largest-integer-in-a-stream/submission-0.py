import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        
        # 1. Transform the list into a min-heap in-place
        heapq.heapify(self.heap) 
        
        # 2. Pop smallest elements until only k remain
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # 1. Add the new value to the heap
        heapq.heappush(self.heap, val)
        
        # 2. If the heap size exceeds k, pop the smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # 3. The k-th largest element is now at the root of the min-heap
        return self.heap[0]