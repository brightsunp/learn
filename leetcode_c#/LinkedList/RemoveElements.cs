/**
* Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class RemoveElements : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(RemoveElementsInternal), RemoveElementsInternal(ListNode.SampleDuplicates(), 2));
        }

        private ListNode RemoveElementsInternal(ListNode head, int val)
        {
            var dummy = new ListNode(0);
            dummy.next = head;

            ListNode pre = dummy;
            while (head != null)
            {
                if (head.val == val)
                {
                    pre.next = head.next;
                }
                else
                {
                    // If never hit, pre.next will be returned as well
                    pre = pre.next;
                }
                head = head.next;
            }

            return dummy.next;
        }
    }
}
