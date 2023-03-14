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
            TestOutput(nameof(ReverseInternalRecursive), ReverseInternalRecursive(ListNode.Sample()));

            TestOutput(nameof(ReverseInternalIterative), ReverseInternalIterative(ListNode.Sample()));
        }

        private ListNode ReverseInternalRecursive(ListNode head)
        {
            if (head == null || head.next == null)
            {
                return head;
            }

            ListNode newHead = ReverseInternalRecursive(head.next);
            head.next.next = head;
            head.next = null;

            return newHead;
        }

        private ListNode ReverseInternalIterative(ListNode head)
        {
            ListNode newHead = null;
            while (head != null)
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
