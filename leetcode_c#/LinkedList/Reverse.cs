/**
* Given the head of a singly linked list, reverse the list, and return the reversed list.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class Reverse : Solution
    {
        public override void Run()
        {
            var test1 = ListNode.Sample();
            TestOutput(nameof(ReverseInternalRecursive), ReverseInternalRecursive(test1));

            var test2 = ListNode.Sample();
            TestOutput(nameof(ReverseInternalIterative), ReverseInternalIterative(test2));
        }

        private ListNode ReverseInternalRecursive(ListNode head)
        {
            if (head == null || head.next == null)
            {
                return head;
            }

            var newHead = ReverseInternalRecursive(head.next);
            head.next.next = head;
            head.next = null;

            return newHead;
        }

        private ListNode ReverseInternalIterative(ListNode head)
        {
            ListNode newHead = null;
            while (head != null)
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
