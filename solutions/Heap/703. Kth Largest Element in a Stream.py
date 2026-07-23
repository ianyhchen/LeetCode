import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):        
        min_heap = nums
        # Transform the list into a min-heap in-place in O(N) time
        heapq.heapify(min_heap)

        # Pop the smallest elements until only the k largest elements remain
        while len(min_heap) > k:
            heapq.heappop(min_heap)

        self.min_heap = min_heap
        self.k = k

    def add(self, val: int) -> int:
        # If heap has fewer than k elements, push the new value directly
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        # If value is larger than the k-th largest element (top of min-heap), replace it
        elif val > self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)        

        # The root of the min-heap always stores the k-th largest element overall
        return self.min_heap[0]
        
            
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)