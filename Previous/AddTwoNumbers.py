from typing import Optional

class ListNode:
    def __init__(self, val= 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = None
        carry = 0

        while l1 or l2:
            temp = 0
            lt = Optional[ListNode]
            if l1 and l2:
                temp = l1.val + l2.val + carry
            elif not l1 and l2:
                temp = l2.val + carry
            elif l1 and not l2:
                temp = l1.val + carry

            if temp >= 10:
                carry = 1
                temp -= 10

            if l1.next:
                l1 = l1.next
            else:
                l1 = None
            if l2.next:
                l2 = l2.next
            else:
                l2 = None

            lt = ListNode(temp, None)
            if not l3:
                l3 = lt
            else:
                l3.next = lt

        return l3
    
s = Solution()

# ????
