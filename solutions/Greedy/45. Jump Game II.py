class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0 # The boundary of the current jump range
        max_reach = 0   # The furthest index we can reach from the current range
        n = len(nums)

        # We don't need to process the last element because once we reach
        # or pass it, we are already at the destination.
        for i in range(0, n - 1):
            # Update the maximum reachable index from the current position
            max_reach = max(max_reach, i + nums[i])

            # If we have reached the boundary of the current jump range
            if i == current_end:
                jumps += 1              # We must make another jump
                current_end = max_reach # Update the boundary to the furthest we detected

                # Optimization: If we can already reach the end, we can stop early
                if current_end >= n - 1:
                    break            
        
        return jumps