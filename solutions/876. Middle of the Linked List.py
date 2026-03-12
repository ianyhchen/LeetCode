# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
暴力法，先掃過一遍，找出總數量，再從頭走到中間的節點

import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        count = 0
        while fast.next:
            temp = fast.next.next
            fast = fast.next
            fast.next = temp
            count += 1
        middle = math.ceil(count / 2)
        while middle > 0:
            temp = slow.next.next
            slow = slow.next
            slow.next = temp
            middle -= 1
        return slow
'''

''' 
fast 走兩步,slow 走一步, 當fast走到底時, slow指標會剛好到中間節點
#為什麼這個條件剛好符合？
關鍵在於我們是先移動指標再檢查條件。

當長度為偶數時,fast 最終會越過最後一個節點，變成 NULL。

當 fast 踏入 NULL 的那一瞬間, slow 正好又往前踏了一步，從第一個中點跨到了第二個中點。

小技巧筆記：

如果你想要的是 First Middle(偶數長度時選左邊那個，例如 6 個選 3):
條件會稍微改動，或者通常會判斷 fast.next 與 fast.next.next。但在 LeetCode 中，大多數題目（如歸併排序 Merge Sort)預設都是找 Second Middle。
'''

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


