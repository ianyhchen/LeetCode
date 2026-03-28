class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []  
        if not digits:
            return res

        letter_map = {
            "2": ["a", "b", "c"],
            "3": ["d","e","f"],
            "4": ["g","h","i"],
            "5": ["j","k","l"],
            "6": ["m","n","o"],
            "7": ["p","q","r", "s"],
            "8": ["t","u","v"],
            "9": ["w","x","y", "z"]
        }
        
        def dfs(index, path):
            # 1. 終止條件：如果 index 走到底了, index用來控制每組合的字元數
            if index == len(digits):
                # 存入res前再join，節省string+string花費
                res.append("".join(path))
                return 

            # 2. 找出當前數字對應哪些字母
            char_list = []
            if digits[index] in letter_map:
                char_list = letter_map[digits[index]]
                
            # 3. 遍歷這些字母
            for c in char_list:
                path.append(c)
                dfs(index + 1, path)
                path.pop()

        dfs(0,[])

        return res
            
