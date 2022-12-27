/**
 * Definition for singly-linked list.
 */
using System.Collections.Generic;

namespace TestMain.Definitions
{
    public class ListNode
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

        public static ListNode SampleIntersect()
        {
            var node1 = new ListNode(5);
            var node2 = new ListNode(4, node1);
            var node3 = new ListNode(3, node2);
            var node4 = new ListNode(6, node3);
            var node5 = new ListNode(7, node4);

            // 8 -> 7 -> 6 -> 3 -> 4 -> 5
            return new ListNode(8, node5);
        }

        public static ListNode SampleSorted()
        {
            var node1 = new ListNode(8);
            var node2 = new ListNode(7, node1);
            var node3 = new ListNode(6, node2);
            var node4 = new ListNode(5, node3);
            var node5 = new ListNode(3, node4);

            // 1 -> 3 -> 5 -> 6 -> 7 -> 8
            return new ListNode(1, node5);
        }
    }
}
