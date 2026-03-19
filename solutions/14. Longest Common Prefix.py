'''
垂直掃描 (Vertical Scanning)
從頭比較所有字串的第一個字元，若都相同，再比較第二個，以此類推。 只要找到第一個不相同的字元，就能終止
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Edge case: if the input list is empty, return an empty string
        if not strs:
            return ""

        # Take the first string as the reference for comparison
        # We will iterate through each character of the first string
        for i in range(len(strs[0])):
            temp_char = strs[0][i]

            # Compare this character with the same index in all other strings
            for j in range(1, len(strs)):
                # If the current index 'i' exceeds the length of the string strs[j]
                # or the character at index 'i' does not match, return the prefix found so far
                if i == len(strs[j]) or strs[j][i] != temp_char:
                    return strs[0][:i]
        
        return strs[0] 
