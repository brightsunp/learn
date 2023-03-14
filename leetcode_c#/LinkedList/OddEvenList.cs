/**
* Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list. 
* 
* The first node is considered odd, and the second node is even, and so on. 
* Note that the relative order inside both the even and odd groups should remain as it was in the input. 
* You must solve the problem in O(1) extra space complexity and O(n) time complexity.
* The number of nodes in the linked list is in the range [0, 10^4].
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class OddEvenList : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(OddEvenList), OddEvenListInternal(ListNode.Sample()));
        }

        private ListNode OddEvenListInternal(ListNode head)
        {
            var dummy1 = new ListNode(0);
            var dummy2 = new ListNode(0);
            ListNode pre1 = dummy1, pre2 = dummy2;
            int pos = 1;
            while (head != null)
            {
                if (pos % 2 == 1)
                {
                    pre1.next = head;
                    pre1 = pre1.next;
                }
                else
                {
                    pre2.next = head;
                    pre2 = pre2.next;
                }

                head = head.next;
                pos++;
            }
            pre1.next = dummy2.next;
            pre2.next = null;

            return dummy1.next;
        }
    }
}
