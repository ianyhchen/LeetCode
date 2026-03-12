'''
hashtable
space complexity O(n) solution

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashtable = {}
        for i in nums:
            hashtable[i] = hashtable.get(i, 0) + 1
            if hashtable[i] > (len(nums) / 2):
                return i
'''

# space complexity O(1) solution
#用兩個變數來記錄次數跟目前的結果，因為題目限制majorityElement一定存在，
#所以跟其他數字比較到最後，majorityElement 一定會剩下
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = majority = 0
        for i in nums:
            if majority == 0:
                res = i
            if i == res:
                majority += 1
            else:
                majority -= 1

        return res
