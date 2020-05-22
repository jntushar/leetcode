/*
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
 */


// ---SOLUTION---

public class Solution {
    public ListNode oddEvenList(ListNode head) {
        if (head == null) {
            return head;
        }
        boolean odd = true;
        ListNode dummyOddHead = new ListNode(0); // for odd nodes
        ListNode curOdd = dummyOddHead;
        ListNode dummyEvenHead = new ListNode(0); // for even nodes
        ListNode curEven = dummyEvenHead;
        while (head != null) {
            ListNode next = head.next;
            head.next = null;
            if (odd) {
                curOdd.next = head;
                curOdd = curOdd.next;
            } else {
                curEven.next = head;
                curEven = curEven.next;
            }
            odd = !odd;
            head = next;
        }
        curOdd.next = dummyEvenHead.next; // merge 2 lists
        return dummyOddHead.next;
    }
}