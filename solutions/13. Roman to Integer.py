class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and hashmap[s[i]] < hashmap[s[i + 1]]:
                result -= hashmap[s[i]]
            else:
                result += hashmap[s[i]]

        return result
                


# 由後往前，記錄前一個值
class Solution:
    def romanToInt(self, s: str) -> int:
        symbol_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        last_val = 0
        for i in reversed(s):
            current_val = symbol_map[i] 
            if  current_val < last_val:
                res -= current_val
            else:
                res += current_val
            last_val = current_val
        return res
