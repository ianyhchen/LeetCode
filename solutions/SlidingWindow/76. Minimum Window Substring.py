from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_map, window = Counter(t), defaultdict(int)  

        required = len(char_map)
        left, match = 0, 0
        # 記錄最小視窗的起始位置與長度
        start = 0
        # 2. Use infinity to handle cases where no window is found
        min_len = float('inf')

        # 外層迴圈：擴張右邊界
        for right in range(len(s)):
            char = s[right]

            # 1. 更新視窗內的資料
            if char in char_map:
                window[char] += 1
                if window[char] == char_map[char]:
                    match += 1
            
            # 內層迴圈：當視窗滿足條件時，嘗試縮小左邊界
            while match == required:
                # 2. 更新最終答案（記錄最小值）
                if right - left + 1 < min_len:
                    start = left
                    min_len = right - left + 1
                
                char_l = s[left]
                # 3. Move left pointer
                if char_l in char_map:                    
                    if window[char_l] == char_map[char_l]:
                        match -= 1
                    window[char_l] -= 1
                left += 1
        
        # 4. If min_len was never updated, return ""
        return "" if min_len == float('inf') else s[start: start + min_len]



            

        