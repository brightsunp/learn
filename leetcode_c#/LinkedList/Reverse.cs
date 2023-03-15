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
            TestOutput(nameof(ReverseRecursive), ReverseRecursive(ListNode.Sample()));
            TestOutput(nameof(ReverseIterative), ReverseIterative(ListNode.Sample()));
        }

        private ListNode ReverseRecursive(ListNode head)
        {
            if (head == null || head.next == null)
            {
                return head;
            }

            ListNode newHead = ReverseRecursive(head.next);
            head.next.next = head;
            head.next = null;

            return newHead;
        }

        private ListNode ReverseIterative(ListNode head)
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
