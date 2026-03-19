'''
使用 Hash Map (字典) 實作子節點
優點：空間效率較高，只會儲存確實出現過的字元，且擴充性強（可處理 Unicode 或各類符號）。

缺點: Hash 運算會有微小的額外開銷。
'''
class TrieNode:
    def __init__(self):
        # Using a dictionary to store child nodes
        # Key: character (str), Value: TrieNode object
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
               
    #從根節點開始，逐一檢查字元的子節點是否存在，不存在則建立新節點。最後一個字元標記為 True
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr =  curr.children[c]
        curr.is_end_of_word = True

    #沿著路徑走，若路徑中斷則回傳 False；走到結尾後，必須確認 isEndOfWord 為 True
    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr =  curr.children[c]

        return curr.is_end_of_word
        
    #邏輯與 Search 類似，但最後不需要檢查 isEndOfWord，只要路徑完整走完即代表前綴存在
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr =  curr.children[c]
            
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''
使用 Array (陣列) 實作子節點
優點：存取速度極快（$O(1)$），適合字元集固定且較小的場景（如 $a-z$）。
缺點：如果字元分布稀疏，會浪費大量空間
'''

class TrieNode:
    def __init__(self):
        # Create an array of size 26, initially all None
        # Each index represents a character (0=a, 1=b, ..., 25=z)
        self.children = [None] * 26
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
               
    #從根節點開始，逐一檢查字元的子節點是否存在，不存在則建立新節點。最後一個字元標記為 True
    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            # Calculate the array index (0 to 25)
            index = ord(c) - ord('a')
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr =  curr.children[index]
        curr.is_end_of_word = True

    #沿著路徑走，若路徑中斷則回傳 False；走到結尾後，必須確認 isEndOfWord 為 True
    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            # Calculate the array index (0 to 25)
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr =  curr.children[index]

        return curr.is_end_of_word
        
    #邏輯與 Search 類似，但最後不需要檢查 isEndOfWord，只要路徑完整走完即代表前綴存在
    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            # Calculate the array index (0 to 25)
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return False
            curr =  curr.children[index]
            
        return True