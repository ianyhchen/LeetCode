class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def dfs(index, path):
            res.append(path[:])

            for i in range(index, len(nums)):
                # 確保是在同一個樹層進行橫向比較。
                # 如果是往深處遞迴 i == index，代表我們正在建立同一個子集（樹枝），此時相同元素是被允許的
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                dfs(i + 1, path)
                path.pop()
        
        dfs(0, [])
        return res