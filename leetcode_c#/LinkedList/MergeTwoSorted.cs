/**
* Merge two sorted lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
* Return the head of the merged linked list.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class MergeTwoSorted : Solution
    {
        public override void Run()
        {
            var test1 = ListNode.Sample();
            var test2 = ListNode.SampleSorted();
            TestOutput(nameof(MergeTwoSortedInternal), MergeTwoSortedInternal(test1, test2));
        }

        private ListNode MergeTwoSortedInternal(ListNode list1, ListNode list2)
        {
            var dummy = new ListNode(0);
            var pre = dummy;

            while (list1 != null && list2 != null)
            {
                if (list1.val < list2.val)
                {
                    pre.next = list1;
                    list1 = list1.next;
                }
                else
                {
                    pre.next = list2;
                    list2 = list2.next;
                }
                pre = pre.next;
            }

            if (list1 != null)
            {
                pre.next = list1;
            }
            if (list2 != null)
            {
                pre.next = list2;
            }

            return dummy.next;
        }
    }
}
