# Time complexity: O(n * 2**n), 每個subset使用大約O(n)的複雜度在copy
# Space complexity: O(n)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []       
        
        def dfs(start_index, path):
            # 1. Add a copy of the current path to the result.
            # We use path[:] to create a shallow copy, otherwise 
            # all entries in res would point to the same list object.
            res.append(path[:])

            # 2. Iterate through the candidate numbers starting from start_index.
            # This ensures we only move forward and avoid generating duplicate sets 
            # like [1, 2] and [2, 1].
            for i in range(start_index, len(nums)):
                # 3. Choose: Add the current number to our current subset path.
                path.append(nums[i])

                # 4. Explore: Move to the next index to build further subsets.
                # Notice we pass i + 1, not start_index + 1.
                dfs(i + 1, path)

                # 5. Backtrack: Remove the last element to "reset" the state 
                # before the next iteration of the loop.
                path.pop()
                
        # Start the recursion with an empty path from the first index.
        dfs(0, [])

        return res


# 迭代解法

'''
Time complexity: O(n * 2**n)
Space complexity: O(n* 2**n)

與 Backtracking 相比，迭代法的優勢在於：

- 沒有遞迴深度限制：不需要擔心 Stack Overflow。

- 邏輯單純：不需要「恢復現場」(pop)，因為我們是基於舊有的列表創建新的列表。

- 缺點：如果題目有複雜的約束（例如子集總和必須等於 K），迭代法很難進行「剪枝」，效率會不如 Backtracking。
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]   

        # for num in nums:
        #     size = len(res)
        #     for i in range(size):
        #         subset = res[i] + [num]
        #         res.append(subset)      
        for num in nums:
            # For each existing subset, create a new subset by adding 'num'
            # and extend the original 'res' list with these new subsets.
            res += [curr + [num] for curr in res]


        return res