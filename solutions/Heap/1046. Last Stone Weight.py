import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Python defaults to min-heap, so invert weights to simulate a max-heap
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop the two heaviest stones (convert back to positive numbers for clarity)
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
            # If they are not equal, the remaining piece goes back to the heap
            if x != y:
                new_weight = x - y
                heapq.heappush(max_heap, -new_weight)
        # If one stone is left, convert it back to positive; otherwise, return 0
        return -max_heap[0] if max_heap else 0
