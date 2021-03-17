/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        HashMap<Node, Node> map = new HashMap<>();
        Node dummy = new Node(0);
        dummy = head;
        //put every node and clone into the hashmap:
        while(dummy != null){
            Node clone = new Node(dummy.val);
            map.put(dummy, clone);
            dummy = dummy.next;
        }
        dummy = head;
        // Map.Entry objects are valid only for the duration of the iteration
        for (Map.Entry<Node,Node> entry : map.entrySet()){
            Node org = entry.getKey();
            Node copy = entry.getValue();
            copy.next = map.get(org.next);
            copy.random = map.get(org.random); //retrieve clone of org's random
        }
        return map.get(head);
    }
}