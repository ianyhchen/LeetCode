import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif len(heap) == k and heap[0] < num:
                heapq.heappushpop(heap, num)
        
        return heap[0]