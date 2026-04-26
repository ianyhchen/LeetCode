class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end_of_word = False        
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()                
            
            curr = curr.children[index]
        curr.is_end_of_word = True
        

    def search(self, word: str) -> bool:       
        def dfs(node, index):
            # Base Case: 字串檢查完了
            if index == len(word):
                return node.is_end_of_word
            
            char = word[index]

            if char == '.':
                # 遍歷 26 個子節點
                for child in node.children:
                    if child: # 如果子節點存在
                        # 只要有一條路通，就回傳 True
                        if dfs(child, index + 1):
                            return True                
                return False
            else:
                i = ord(char) - ord('a')
                child = node.children[i]
                if child:
                    # 這裡的關鍵：必須把「後面剩下的搜尋結果」傳回來
                    return dfs(child, index + 1)
                else:
                    return False              
        
        return dfs(self.root, 0)



                
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)