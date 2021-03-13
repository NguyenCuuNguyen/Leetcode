#You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None or l2 is None:
            return None
        head = result = ListNode(0)
        total = 0
        while l1 or l2 or total:
            #val = head1.val + head2.val
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            result.next = ListNode(total % 10)
            result = result.next
            total //= 10 #handled both cases where carry = 0 and where carry is not 0.

        return head.next # <= head.val = 0 

#Learn from Alternative solutions:
#(1) Chained assignment: n = n.next = ListNode(val) means first n = ListNode(val) , now the n is ListNode(val), then n.next point to the address ListNode(val) which means point to itself!!!
#(2) carry, val = divmod(v1+v2+carry, 10)