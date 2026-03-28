'''
拓撲排序剝洋蔥法 (Optimal)
思路：
- 找出所有葉子節點（度數為 1 的節點）。
- 將這些葉子節點從圖中移除，並更新與它們相鄰節點的度數。
- 產生新的葉子節點，重複此過程。
- 當剩下的節點數量 <= 2 時，這些節點就是最小高度樹的根。
複雜度：O(n)。每個節點和每條邊都只被處理過常數次。
'''

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = [set() for _ in range(n)]

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)        
        
        leaves = []
        for i in range(n):
            if len(adj[i]) == 1:
                leaves.append(i)
        # 最小高度樹（MHT）的根節點只會是 1 個或 2 個, (偶數節點可能有兩個根節點)，
        # 若有三個的話，其中必有葉子節點可以繼續被剪掉，直到剩下 1 或 2 個
        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for leaf in leaves:
                if not adj[leaf]:
                    continue

                # 因為 leaf 是葉子，它在 adj[leaf] 裡只會有一個鄰居
                # 我們用 pop() 把這唯一的鄰居拿出來（順便清空該葉子的鄰接表）
                neighbor = adj[leaf].pop()

                # 因為葉子不見了，鄰居的鄰接表也要移除該葉子
                adj[neighbor].remove(leaf)

                # 判斷鄰居是否變成新的葉子
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves 
        
        