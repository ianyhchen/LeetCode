class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        # Sort the array to use two pointers and handle duplicates easily
        nums.sort()

        for i in range(len(nums)):
            # Optimization: If the current smallest number is > 0, 
            # no triplet can sum to 0 anymore.
            if nums[i] > 0:
                break

            # Deduplication for the first element (i)
            # Skip if the current number is the same as the previous one
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Deduplication for the second (L) and third (R) elements
                    # Skip all identical elements to avoid duplicate triplets
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Crucial: Move both pointers simultaneously to find new potential sums
                    left += 1
                    right -= 1

        return res


       
