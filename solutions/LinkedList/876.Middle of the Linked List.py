# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
延伸思考：如果要找的是「第一個中間點」怎麼辦？
如果今天面試官壞壞，改了題目說：「如果是偶數長度，我想回傳第一個中間點（也就是 6 個節點要回傳 3）」呢？

這時候我們有兩種改法：

改動判斷條件： 我們可以偷看快指標「下兩步」是不是空的。迴圈條件改成 while fast.next and fast.next.next:。這樣在偶數長度時，快指標就會少走一步，慢指標就會剛好停在 3。

直覺改法（推薦）： 或者是，我們讓 fast 初始在 head.next（領先一步出發），slow 一樣在 head，維持原本的 while 條件，最後 slow 就會停在第一個中間點。
'''
import math
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
