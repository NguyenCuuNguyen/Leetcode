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
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        
        while (cur != null){ //keep comparing node with next, with multiple duplicates
            if (cur.next == null) break; //take care of 1 node case
            if(cur.val == cur.next.val){
                cur.next = cur.next.next;
            }else{
                cur = cur.next;
            }
        }
        return head;
    }
}

//Failed 1st attempt:
// while (cur != null && cur.next != null){
            
//             if(cur.val == cur.next.val){
//                 cur.next = (cur.next.next == null) ? null : cur.next.next;
//             }
//             if(cur.val == lastVal) 
//             lastVal = cur.val;
//             cur = cur.next; 
//         }
//=> Don't move cur if we don't know if cur.next has the 