'''
任何一個矩形的高度，必然是由參與該矩形的柱子中「最矮的那一根」決定的。
因此，我們的目標是：對於每一根柱子 i，計算以其高度 H_i 為基準，向左和向右最遠能擴展到哪裡。

Monotonic Stack, 棧內索引對應的高度保持 嚴格遞增 或 非遞減
當我們遍歷柱子時，如果當前柱子比棧頂柱子矮，說明棧頂柱子的「右邊界」找到了。而棧頂柱子的「左邊界」就是它在棧中的前一個元素
時間複雜度： O(n)，每根柱子最多進棧一次、出棧一次。
空間複雜度： O(n)，用於存儲棧

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Sentinel trick
        heights = [0] + heights + [0]

        stack = [0]
        max_area = 0
        for i in range(1, len(heights)):
            # 這裡必須用 while，因為當前高度可能觸發連續多個柱子的結算
            while stack and heights[i] < heights[stack[-1]]:          
                mid = stack.pop()
                left_index = stack[-1]
                area = heights[mid] * (i - left_index - 1)
                max_area = max(max_area, area)

            # 結算完所有比自己高的柱子後，把自己放進去
            stack.append(i)                
        
        return max_area

