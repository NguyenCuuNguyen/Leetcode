class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
    
        head1 = head
        head2 = head.next
        evenHead = head2
        #Use even head as condition bc it's ahead of odd
        while head2 != None and head2.next != None:
            head1.next = head1.next.next
            head2.next = head2.next.next
            head1 = head1.next
            head2 = head2.next
        #head1 is the last element in odd list
        head1.next = evenHead
        return head