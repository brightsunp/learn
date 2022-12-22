/**
 * Definition for singly-linked list.
 */
using System.Collections.Generic;

namespace TestMain.Definitions
{
    class ListNode
    {
        public int val;
        public ListNode next;

        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }

        public override string ToString()
        {
            var res = new List<int>();
            var cur = this;
            while (cur != null)
            {
                res.Add(cur.val);
                cur = cur.next;
            }

            return string.Join(" -> ", res);
        }

        public static ListNode Sample()
        {
            var node1 = new ListNode(5);
            var node2 = new ListNode(4, node1);
            var node3 = new ListNode(3, node2);
            var node4 = new ListNode(2, node3);

            // 1 -> 2 -> 3 -> 4 -> 5
            return new ListNode(1, node4);
        }
    }
}
