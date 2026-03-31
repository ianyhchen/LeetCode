from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        # max_heap stores the smaller half of the numbers (inverted to simulate max-heap)
        self.max_heap = []
        # min_heap stores the larger half of the numbers
        self.min_heap = []


    def addNum(self, num: int) -> None:
        # Step 1: Push to max_heap first (inverted)
        heappush(self.max_heap, -1 * num)

        # Step 2: Pop the largest from max_heap and move it to min_heap
        # This ensures min_heap always gets a value larger than anything in max_heap
        largest_from_left = heappop(self.max_heap)
        heappush(self.min_heap, -largest_from_left)

        # Step 3: Rebalance if min_heap becomes larger than max_heap
        # We maintain: len(max_heap) >= len(min_heap)
        if len(self.min_heap) > len(self.max_heap):
            smallest_from_right = heappop(self.min_heap)
            heappush(self.max_heap, -smallest_from_right)


    def findMedian(self) -> float:
        left_len = len(self.max_heap)
        right_len = len(self.min_heap)
        
        if (left_len + right_len) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:            
            return float(-self.max_heap[0])
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

# Insertion sort solution, addNum O(n) complexity
class MedianFinder:

    def __init__(self):       
        self.store = []
       

    def addNum(self, num: int) -> None:
        # Step 1: Find the correct insertion point using binary search
        index = self.binarySearch(num)
        # Step 2: Insert the number into the list (O(N) operation)
        self.store.insert(index, num)        


    def findMedian(self) -> float:
        n = len(self.store)
        if n % 2 == 0:
            return (self.store[n // 2 - 1] + self.store[n // 2]) / 2.0
        else:            
            return float(self.store[n // 2])
        
    def binarySearch(self, num: int) -> int:
        # Left-closed, Right-open interval [left, right)
        # 新數字有可能比目前陣列中所有的數字都大，這時它應該被插入在索引 len(store) 的位置。如果 right 只設到 len-1，永遠找不到最後一個位置
        left, right = 0, len(self.store)

        while left < right:
            mid = left + (right - left)//2
            if self.store[mid] < num:
                # Target is in the right half, exclude mid
                left = mid + 1
            else:
                # Target could be at mid or in the left half, include mid
                right = mid
        return left