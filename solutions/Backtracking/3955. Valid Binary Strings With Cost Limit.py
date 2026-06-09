class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        comb = []
        def backtrack(index, current_string, current_cost):
            # Pruning: if current cost already exceeds k, stop searching
            if current_cost > k:
                return
            # Base case: successfully constructed a valid string of length n
            if index == n:
                comb.append(current_string)
                return 
                
            # Choice 1: Append '0' (Always valid, cost does not increase)
            backtrack(index + 1, current_string + '0', current_cost)

            # Choice 2: Append '1' 
            # Condition 1: Cannot have two consecutive '1's
            # Condition 2: New cost after adding '1' at 'index' must be <= k
            if (not current_string or current_string[-1] != '1') and current_cost + index <= k:
                backtrack(index + 1, current_string + '1', current_cost + index)
        # Start backtracking from index 0 with an empty string and 0 cost
        backtrack(0, "", 0)

        return comb
        