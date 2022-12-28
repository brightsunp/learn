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
            var test1 = ListNode.Sample();
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(test1, 1, 2));

            var test2 = ListNode.Sample();
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(test2, 2, 2));

            var test3 = ListNode.Sample();
            TestOutput(nameof(ReverseBetweenInternal), ReverseBetweenInternal(test3, 2, 4));
        }

        private ListNode ReverseBetweenInternal(ListNode head, int left, int right)
        {
            var dummy = new ListNode(0, head);
            var pre = dummy;
            for (int i = 0; i < left - 1; i++)
            {
                pre = pre.next;
            }
            var start = pre.next;
            var end = start.next;
            for (int i = 0; i < right - left; i++)
            {
                end = end.next;
            }

            var newHead = ReverseInternal(start, end);
            pre.next = newHead;

            return dummy.next;
        }

        private ListNode ReverseInternal(ListNode head, ListNode end)
        {
            var newHead = end;
            while (head != end)
            {
                var tmp = head.next;
                head.next = newHead;
                newHead = head;
                head = tmp;
            }

            return newHead;
        }
    }
}
