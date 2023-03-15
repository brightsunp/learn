/**
* Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list. 
* 
* k is a positive integer and is less than or equal to the length of the linked list. 
* If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is. 
* You may not alter the values in the list's nodes, only nodes themselves may be changed. 1 <= k <= n <= 5000.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class ReverseKGroup : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(ReverseKGroupInternal), ReverseKGroupInternal(ListNode.Sample(), 1));
            TestOutput(nameof(ReverseKGroupInternal), ReverseKGroupInternal(ListNode.Sample(), 2));
            TestOutput(nameof(ReverseKGroupInternal), ReverseKGroupInternal(ListNode.Sample(), 3));
            TestOutput(nameof(ReverseKGroupInternal), ReverseKGroupInternal(ListNode.Sample(), 4));
            TestOutput(nameof(ReverseKGroupInternal), ReverseKGroupInternal(ListNode.Sample(), 5));
        }

        private ListNode ReverseKGroupInternal(ListNode head, int k)
        {
            var dummy = new ListNode(0, head);
            ListNode pre = dummy, start = head;
            int pos = 1;
            while (head != null)
            {
                if (pos % k == 0)
                {
                    // head gets changed in reverse helper
                    pre.next = ReverseHelper(start, head.next);
                    for (int i = 0; i < k; i++)
                    {
                        pre = pre.next;
                    }
                    head = pre.next;
                    start = head;
                }
                else
                {
                    head = head.next;
                }
                pos++;
            }
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
