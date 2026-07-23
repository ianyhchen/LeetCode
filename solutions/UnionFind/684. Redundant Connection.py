class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        # 1. 初始化 parent 陣列（節點編號為 1 ~ n，所以長度設 n + 1）
        parent = [i for i in range(n +1)]

        def find(i :int):
            # 如果 i 的父節點就是自己，代表 i 就是根節點
            if parent[i] == i:
                return i

            # 路徑壓縮：在遞迴找根節點的同時，直接將目前節點 parent[i] 更新為最高根節點
            parent[i] = find(parent[i])
            return parent[i]

        def union(u: int, v: int) -> bool:
            # 1. 先找出兩者的最高根節點
            root_u = find(u)
            root_v = find(v)

            # 2. 判斷是否已經在同一個集合（是否形成環）
            if root_u == root_v:
                return False # 合併失敗，代表 u 與 v 已經連通，加入這條邊會產生環！
            
            # 3. 合併集合：讓其中一個根節點指向另一個根節點
            parent[root_u] = root_v
            return True

        # 2. 依序檢查每一條邊
        for u,v in edges:
            # 嘗試 union 兩點，若 return False 代表兩點早已連通，此邊即為冗餘邊！
            if not union(u, v):
                return [u, v]
