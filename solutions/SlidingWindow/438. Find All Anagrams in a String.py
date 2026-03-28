from collections import defaultdict
# Sliding window solution
# Time complexity O(n), space: O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count, s_count = [0] * 26, [0] * 26
        s_len, p_len = len(s), len(p)
        res = []

        # Boudary check
        if p_len > s_len:
            return res
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1

        # Initialize first window
        for i in range(0, p_len):
            s_count[ord(s[i]) - ord('a')] += 1
        
        if p_count == s_count:
            res.append(0)
        
        # 從第一個視窗開始往後移動, i 代表目前新加入視窗的位置, 每次一進一出
        for i in range(p_len, s_len):
            # window range: [i - p_len + 1, i]
            s_count[ord(s[i]) - ord('a')] += 1  #進場
            s_count[ord(s[i - p_len]) - ord('a')] -= 1  #最左邊數字退場

            if s_count == p_count:
                res.append(i - p_len + 1)

        return res
