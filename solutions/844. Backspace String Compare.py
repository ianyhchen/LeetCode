'''
Stack solution
遍歷字串，遇字符入棧，遇 # 則彈出棧頂。最後比較兩個結果字串。
time & space complexity: O(n + m)
'''


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Define a helper function
        def process(string: str) -> list:
            stack = []
            for c in string:
                if c != '#':
                    stack.append(c)
                elif stack: # More pythonic way to check if stack is not empty
                    stack.pop()
            return stack       
        
        return process(s) == process(t)
    

'''
Two Pointers
從字串末尾開始向前遍歷。遇到 # 就計數，跳過接下來的字符
time complexity: O(n + m)
space complexity: O(1)
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1        
        def get_next_valid(string: str, index: int) -> int:
            skip = 0
            while index >= 0:
                if string[index] == '#':
                    skip += 1
                    index -= 1
                elif skip > 0:
                    skip -= 1
                    index -= 1
                else:
                    break
            return index

        while i >= 0 or j >= 0:
            # Find the next valid character
            i = get_next_valid(s, i)
            j = get_next_valid(t, j)
           
            # Compare the current valid characters
            # Check if one string is exhausted while the other is not
            if (i >= 0) != (j >= 0):
                return False

            # If both have valid characters, compare them
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            # Move pointers to continue searching
            i -= 1
            j -= 1
        return True