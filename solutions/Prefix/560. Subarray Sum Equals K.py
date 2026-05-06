'''
前綴和 (Prefix Sum)：利用 P[j] - P[i-1] = k 的數學特性，將區間和問題轉化為差值問題。
雜湊表 (Hash Map)：空間換時間。用來儲存各個「前綴和」出現過的次數，將時間複雜度優化至 O(n)。
'''
from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count: stores the total number of valid subarrays
        # current_sum: stores the cumulative sum while iterating
        count, current_sum  = 0, 0

        # prefix_map: stores frequency of each prefix sum encountered
        # Initialize with {0: 1} to handle cases where current_sum itself equals k
        prefix_map = defaultdict(int)
        prefix_map[0] = 1 # 代表「和為 0 的前綴」已經出現過 1 次（即空陣列的情況）

        for num in nums:
            # Update the running prefix sum
            current_sum += num

            # If (current_sum - k) exists in map, it means there are 
            # prefix_map[current_sum - k] subarrays ending here that sum to k
            if current_sum - k in prefix_map:
                count += prefix_map[current_sum - k]               
           
            # Always update the map with the current_sum frequency
            prefix_map[current_sum] += 1

        return count

        