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
        ListNode temp = new ListNode(0);
        temp.next = head;
        //use two pointers, slow - track the node before the dup nodes, 
	// fast - to find the last node of dups.
        ListNode fast = temp;
        ListNode slow = temp;
        fast = slow.next; //fast points to first node
        ListNode cur = temp;

        while(fast != null){
            while(fast.next != null && fast.val == fast.next.val){//find the last dup node
                fast = fast.next;
            } 
            if(slow.next != fast){ 
                slow.next = fast.next;
             //   slow = slow.next; //if moved slow, couldn't check if duplicate.next is duplicate or not with fast
                fast = slow.next;
            }else{
                slow = slow.next;
                fast = fast.next;
            }
            
        }
        return temp.next;
    }
}

// if(cur.next.val == cur.next.next.val){
//                 val = cur.next.val;
//                 cur.next = cur.next.next.next; 
//             }else if (cur.val = ){
                
//             }else{
//                 cur = cur.next;
//             }