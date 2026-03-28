from collections import defaultdict
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Tasks = max(len(tasks), (max_freq - 1) * (n + 1) + n_max), n_max = same max_freq count
        freq_map = defaultdict(int)
        
        max_freq = 0
        for t in tasks:
            freq_map[t] += 1
            max_freq = max(max_freq, freq_map[t])
        # Find how many tasks have the same maximum frequency
        # e.g., if A:3, B:3, then n_max = 2
        same_max_count = 0
        for v in freq_map.values():
            if v == max_freq:
                same_max_count += 1
        # Calculate the total slots based on the "bucket" logic
        # (max_freq - 1) is the number of full chunks
        # (n + 1) is the size of each chunk (1 task + n idles)
        # n_max is the number of tasks in the very last partial chunk

        # If the number of tasks is larger than our calculated slots,
        # it means no idle time is needed. Return the total number of tasks.
        res = max(len(tasks), (max_freq - 1) * (n + 1) + same_max_count)
        return res
        
        

from collections import defaultdict
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:      
        freq_map = defaultdict(int)
        for t in tasks:
            freq_map[t] += 1

        # Use a max-heap to store task frequencies (using negative values for Python's min-heap)
        # 存放「當前所有可執行」的任務，並按頻率排序
        max_heap = [-v for v in freq_map.values()]
        heapq.heapify(max_heap)

        time = 0
        # Queue stores: (remaining_count, time_when_available)
        # 存放「暫時不能執行」的任務，並按「解禁時間」排序。
        queue = deque()

        while max_heap or queue:
            time += 1

            if max_heap:
                # Execute the most frequent available task
                count = heapq.heappop(max_heap) + 1 # +1 because it's negative, 不須特別轉回正數
                if count != 0:
                    # Task is not finished, add it to the cooling queue
                    queue.append((count, time + n))
                    
            # Check if any task in the queue has finished its cooling period
            if queue and queue[0][1] == time:
                # Move the task back to the max-heap
                count, unlock_time = queue.popleft()
                heapq.heappush(max_heap, count)
                  
        return time
        
        