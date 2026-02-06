#用magazine字元個數建立hashtable，用來ransomNote中每個字元是否都可以包含在內
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
            
        hashtable = {}
        for i in magazine:
            hashtable[i] = 1 + hashtable.get(i, 0) # use get to prevent key error
               
        for i in ransomNote:
            if i not in hashtable or hashtable[i] <= 0:
                return False
            else:
                hashtable[i] -= 1        
        return True