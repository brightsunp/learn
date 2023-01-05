/**
* You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
* Merge all the linked-lists into one sorted linked-list and return it.
*/
using TestMain.Definitions;

namespace TestMain.Sort
{
    class MergeKLists : Solution
    {
        public override void Run()
        {
            var test = new ListNode[] { ListNode.Sample(), ListNode.SampleSorted(), ListNode.SampleSorted() };
            TestOutput(nameof(MergeKListsReduce), MergeKListsReduce(test));

            test = new ListNode[] { ListNode.Sample(), ListNode.SampleSorted(), ListNode.SampleSorted() };
            TestOutput(nameof(MergeKListsDivide), MergeKListsDivide(test));
        }

        // Only leverage the merge part from MergeSort
        private ListNode MergeKListsReduce(ListNode[] lists)
        {
            ListNode res = null;
            for (int i = 0; i < lists.Length; i++)
            {
                res = MergeTwoLists(res, lists[i]);
            }

            return res;
        }

        // Leverage both the divide part and merge part from MergeSort
        private ListNode MergeKListsDivide(ListNode[] lists)
        {
            if (lists.Length == 0)
            {
                return null;
            }

            return MergeKListsDivideInternal(lists, 0, lists.Length - 1);
        }

        private ListNode MergeKListsDivideInternal(ListNode[] lists, int left, int right)
        {
            if (left == right)
            {
                return lists[left];
            }

            int mid = (left + right) >> 1;
            ListNode l = MergeKListsDivideInternal(lists, left, mid);
            ListNode r = MergeKListsDivideInternal(lists, mid + 1, right);
            return MergeTwoLists(l, r);
        }

        private ListNode MergeTwoLists(ListNode list1, ListNode list2)
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
