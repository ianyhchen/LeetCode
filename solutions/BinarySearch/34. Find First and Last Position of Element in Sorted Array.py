class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Handle empty array case to prevent index errors
        if len(nums) == 0:
            return [-1, -1]

        # --- Search for the Left Bound (First Position) ---
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                # If target found, keep searching the left side to find the first occurrence
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        # Check if 'left' index is within bounds AND if the value is the target
        # Important: Check boundary condition 'left < len(nums)' first to avoid IndexError
        ans_left = left if left < len(nums) and nums[left] == target else -1

        # --- Search for the Right Bound (Last Position) ---
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target == nums[mid]:
                # If target found, keep searching the right side to find the last occurrence
                left = mid + 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
                
        # Check if 'right' index is within bounds AND if the value is the target
        # Important: Check boundary condition 'right >= 0' first
        ans_right = right if right >= 0 and nums[right] == target else -1

        return [ans_left, ans_right]