class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(path, open_count, close_count):
            # Base case: if the current path length equals 2 * n, a valid combination is formed
            if len(path) == 2 * n:
                # Join the list of characters into a string and add to the result list
                res.append(''.join(path))
                return

            # If we can still add an opening parenthesis
            if open_count < n:
                path.append('(')
                backtrack(path, open_count + 1, close_count) # Explore: move to the next step
                path.pop() # Backtrack: remove '(' to explore other possibilities
            
            # If we can add a closing parenthesis (must have fewer closing than opening)
            if close_count < open_count:
                path.append(')')
                backtrack(path, open_count, close_count + 1) # Explore: move to the next step
                path.pop() # Backtrack: remove ')' to explore other possibilities
        
        # Start recursion with an empty path and zero counts
        backtrack([], 0, 0)

        return res