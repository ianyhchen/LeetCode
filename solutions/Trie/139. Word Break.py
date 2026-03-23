'''
 複雜度分析與比較
 假設 N 是字串 s 的長度，M 是字典中單詞的總數，K 是單詞的平均長度。
 - Trie 構建：O(M * K) 的時間和空間。
 - DFS 時間複雜度：O(N^2)。
    - 因為有記憶化，dfs 函數最多被調用 N 次。
    - 每次調用中，內層迴圈最多從 p 遍歷到 N。與普通 DP 不同，這裡沒有手動切片 (slice) 操作，Trie 的向下移動是 O(1) 的（在內層迴圈中）。
'''


class TrieNode:
    def __init__(self):
        # Dictionary to store children: {char: TrieNode}
        self.children = {}
        self.is_end_of_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Step 1: Initialize the root of the Trie
        root = TrieNode()

        # Step 2: Build the Trie with all words in wordDict
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_end_of_word = True

        # Step 3: DFS with Memoization to explore valid breaks
        memo = {}
        # s[index:] 
        def dfs(index) -> bool:
            # If we reached the end of the string, it's a successful split 
            if index == len(s):
                return True
            if index in memo:
                return memo[index]
            
            curr = root
            for i in range(index, len(s)):
                char = s[i]
                # If the current character is not in Trie, no further match possible
                if char not in curr.children:
                    break

                # Move to the child node in Trie
                curr = curr.children[char]

                # If a word ends here, recursively check the remaining substring
                if curr.is_end_of_word:
                    if dfs(i + 1):
                        memo[index] = True
                        return True
            memo[index] = False
            return False

        return dfs(0)
        
    
        