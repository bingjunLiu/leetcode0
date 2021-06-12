# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        value=l1.val+l2.val
        ansole = ListNode(value%10)
        ansole.next = self.addTwoNumbers(l1.next,l2.next)

        if value>=10:
            ansole.next=self.addTwoNumbers(ListNode(1),ansole.next)
        return ansole




