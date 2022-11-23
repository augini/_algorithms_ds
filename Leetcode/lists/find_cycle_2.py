# https://leetcode.com/problems/linked-list-cycle-ii/submissions/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow, fast = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                slow_2 = head
                while slow_2 != slow:
                    slow_2 = slow_2.next
                    slow = slow.next

                return slow

        return None
