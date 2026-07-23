# backtracking + two pointer check palindrome
# Time complexity: O(N * 2 ** N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # Helper function using two pointers to check palindromes in the original string 's'
        def is_palindrome(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(index, path):
            # Base Case: If we've reached the end of the string, a valid partitioning is found
            if index == len(s):
                res.append(path[:])
                return

            # Explore all possible partition cut points from 'index' to the end of the string
            for i in range(index, len(s)):       

                if is_palindrome(index, i):
                    # Slice the substring only when we are sure it's a valid palindrome
                    substring = s[index : i + 1]
                    path.append(substring)
                    dfs(i + 1, path)
                    path.pop()
                else:
                    continue

        dfs(0, [])
        return res

# backtracking + two pointer check palindrome + cache
from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        # Helper function using two pointers to check palindromes in the original string 's'
        # 1. Using @cache to memoize the results of palindrome checks.
        # This gives us O(1) lookups for previously seen substrings.
        @cache
        def is_palindrome(left, right) -> bool:
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True

        def dfs(index, path):
            # Base Case: If we've reached the end of the string, a valid partitioning is found
            if index == len(s):
                res.append(path[:])
                return

            # Explore all possible partition cut points from 'index' to the end of the string
            for i in range(index, len(s)):       

                if is_palindrome(index, i):
                    # Slice the substring only when we are sure it's a valid palindrome
                    substring = s[index : i + 1]
                    path.append(substring)
                    dfs(i + 1, path)
                    path.pop()
                else:
                    continue

        dfs(0, [])
        return res
