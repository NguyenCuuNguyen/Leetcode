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
//Method 1: Fast and Slow Pointer
class Solution {
   public ListNode middleNode(ListNode head) {
       ListNode fast = head;
       ListNode slow = head;
       while (fast!= null && fast.next!= null){
           slow = slow.next;
           fast = fast.next.next;
       }
       return slow;
   }
}

//Method 2: Put all nodes into array in order

class Solution {
    public ListNode middleNode(ListNode head) {
       ListNode[] lst = new ListNode[100];
       int i = 0;
        for(i = 0; head.next!=null; i++){
            lst[i] = head;
            head = head.next;
        }
        return lst[i/2]
    }
}