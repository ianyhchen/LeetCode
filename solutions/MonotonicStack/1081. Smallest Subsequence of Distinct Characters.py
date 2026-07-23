from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # Frequency map to track how many times each character appears in the remaining part of the string
        counter = Counter(s)
        # Set to record characters currently sitting in the stack (for O(1) duplicate lookup)
        visited = set()
        # Monotonic stack to build the smallest lexicographical subsequence
        stack = []

        for char in s:
            # Step 1: Decrement the remaining count since the current index moves forward
            counter[char] -= 1

            # Step 2: If the character is already in our stack, skip it to maintain uniqueness
            if char in visited:
                continue
            
            # Step 3: Maintain the monotonic increasing property of the stack.
            # Pop the top element if:
            # 1. The stack is not empty.
            # 2. The top character has a larger alphabetical value than the current character.
            # 3. The top character appears again later in the string (counter > 0).
            while stack and stack[-1] > char and counter[stack[-1]] > 0:
                top = stack.pop()
                visited.remove(top)     # Synchronize with the visited set
            
            # Step 4: Push the current character into the stack and mark it as visited
            stack.append(char)
            visited.add(char)
        
        return ''.join(stack)
