/**
* Given the head of a singly linked list and two integers left and right where left <= right, 
* reverse the nodes of the list from position left to position right, and return the reversed list.
* 
* The number of nodes in the list is n: 1 <= n <= 500, 1 <= left <= right <= n
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class ReverseBetween : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(ListNode.Sample(), 1, 2));
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(ListNode.Sample(), 2, 2));
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(ListNode.Sample(), 2, 4));
        }

        private ListNode ReverseBetweenInternal(ListNode head, int left, int right)
        {
            var dummy = new ListNode(0, head);
            ListNode pre = dummy;
            int pos = 1;
            while (pos < left)
            {
                pre = pre.next;
                pos++;
            }
            ListNode start = pre.next;
            ListNode end = start.next;
            while (pos < right)
            {
                end = end.next;
                pos++;
            }

            pre.next = ReverseHelper(start, end);
            return dummy.next;
        }

        private ListNode ReverseHelper(ListNode head, ListNode tail)
        {
            ListNode newHead = tail;
            while (head != tail)
            {
                ListNode tmp = head.next;
                head.next = newHead;
                newHead = head;
                head = tmp;
            }

            return newHead;
        }
    }
}
