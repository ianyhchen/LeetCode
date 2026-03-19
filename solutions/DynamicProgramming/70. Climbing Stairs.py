class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        dynamic programming : 將大問題拆解成重疊的子問題，並儲存子問題的解以避免重複計算

        要到達第 3 階，你可以從第 2 階跨 1 步，或是從第 1 階跨 2 步。
        這意味著：到達某一層的方法數 = 到達前一層的方法數 + 到達前兩層的方法數。
        類似費式數列 $F(n) = F(n-1) + F(n-2)

        紀錄每階數據，避免重複計算
        時間複雜度: O(n)
        空間複雜度: O(n)
        '''
        table = {}
        table[0] = 1
        table[1] = 1

        for i in range(2, n):
            table[i] = table[i - 1] + table[i - 2]

        return table[n]