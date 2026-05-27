class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # Sort the array to use the two-pointer technique effectively
        nums.sort()
        # Initialize closest_sum with an infinite value or the sum of the first three elements
        closest_sum = float('inf')

        for i in range(len(nums)):            
            # Optimization: Skip the same element to avoid redundant calculations
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Initialize two pointers: left starts after i, right starts at the end
            left, right = i + 1, len(nums) - 1
            while left < right:                
                current_sum  = nums[i] + nums[left] + nums[right]

                # If current_sum is exactly the target, return it immediately
                if current_sum == target:
                    return target

                # Update closest_sum if the current gap is smaller than the recorded gap
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum =  current_sum

                # Move pointers based on the comparison between current_sum and target
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                
        return closest_sum