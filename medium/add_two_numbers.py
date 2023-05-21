# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        num1,num2 = "",""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            num2+= str(l2.val)
            l2 = l2.next

        sumInt = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        
        output = n = ListNode(0)

        for x in sumInt:
            output.next = ListNode(x)
            output = output.next

        return n.next
        
        