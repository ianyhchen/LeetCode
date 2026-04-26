#列表生成式 + 獨立set
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. Initialize 9 sets for each constraint using list comprehension.
        # Note: Avoid [set()] * 9 as it creates references to the same set object.
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                # 2. Skip empty cells
                if val == ".":
                    continue

                # 3. Calculate box index (0-8)
                # Map 2D coordinates (r, c) to 1D box index
                box_index = (r // 3) * 3 + (c // 3)

                # 4. Check if the value already exists in current row, column, or box
                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False
                    
                # 5. Add the value to the corresponding sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True


# 單一Set + tuple
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == ".": continue
                
                if (r, "row", val) in seen or (c, "col", val) in seen or (r // 3, c // 3, "box", val) in seen:
                    return False
                else:
                    seen.add((r, "row", val))
                    seen.add((c, "col", val))
                    seen.add((r // 3, c // 3, "box", val))
        
        return True
