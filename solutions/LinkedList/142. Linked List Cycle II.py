# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
定義 slow 和 fast 兩個指標，初始都指向 head。

slow 每次走 1 步，fast 每次走 2 步。如果 fast 走到結尾（None），代表無環。

如果兩指標相遇，代表有環。

尋找入口：相遇後，將其中一個指標（例如 fast）移回 head，然後兩個指標此時都每次只走 1 步。當它們再次相遇時，相遇點即為環的起點。
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # there is a cycle
            if slow == fast:
                fast = head
                # found the entry location
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow        
        
        return None