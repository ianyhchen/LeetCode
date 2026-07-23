from collections import defaultdict
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
            
        sorted_arr = sorted(arr)

        value_rank_map = defaultdict(int)        
        curr_rank = 0
        for num in sorted_arr:
            if num not in value_rank_map:
                curr_rank += 1
                value_rank_map[num] = curr_rank
        res = []
        for num in arr:
            res.append(value_rank_map[num])
        
        return res
        