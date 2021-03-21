class Solution {
    public ListNode swapPairs(ListNode head) {
    //1's next = 3; 0's next is 2; make 2 points to 1
                                            //head
        ListNode temp = new ListNode(0); //0-->1-->2
        temp.next = head;
        ListNode current = temp;
        while(current.next != null && current.next.next != null){
            ListNode first = current.next;
            ListNode second = current.next.next;
            current.next = second;
            first.next = second.next;
            current.next.next = first;
            current = current.next.next;
        }
        return temp.next;
    }
}