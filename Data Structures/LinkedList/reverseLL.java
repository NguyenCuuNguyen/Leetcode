/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        //Reverse linked List within range:
        ListNode dummy = new ListNode(0); //to keep track of head
        dummy.next = head; //points to the same first node.
        
        ListNode cur1 = dummy;
        ListNode prev1 = null;
        //find starting point to reverse
        for(int i = 0; i<left; i++){//stop when cur points to left.next:
            prev1 = cur1;
            cur1 = cur1.next;
        } 
        
        ListNode cur2 = cur1;
        ListNode prev2 = prev1;
        ListNode q2;
        //reverse every node within range:
        for(int i = left; i<= right; i++){//stop when cur points to right.next:
            q2 = cur2.next;
            cur2.next = prev2;
            prev2 = cur2;
            cur2 = q2;
        } 
        
        prev1.next = prev2;
        cur1.next = cur2;
        
        return dummy.next;

    }
}