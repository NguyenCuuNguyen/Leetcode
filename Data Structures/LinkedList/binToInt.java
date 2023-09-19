public class binToInt {
    public int getDecimalValue(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null){
            sb.append(head.val);
            head = head.next;
        }
        String str = sb.toString();
        int result = Integer.parseInt(str, 2);
        return result;
    }
}
