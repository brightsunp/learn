/**
* Definition for a linked list node with random pointer.
*/
using System.Collections.Generic;

namespace TestMain.Definitions
{
    public class ListNodeWithRandom
    {
        public int val;
        public ListNodeWithRandom next;
        public ListNodeWithRandom random;

        public ListNodeWithRandom(int _val)
        {
            val = _val;
            next = null;
            random = null;
        }

        public override string ToString()
        {
            var res = new List<(int, int)>();
            var cur = this;
            int count = 0;
            while (cur != null && count < 16)
            {
                res.Add((cur.val, (int)cur.random?.val));
                cur = cur.next;
                count++;
            }

            return string.Join(" -> ", res);
        }

        public static ListNodeWithRandom Sample()
        {
            var node1 = new ListNodeWithRandom(5);
            var node2 = new ListNodeWithRandom(4) { next = node1 };
            var node3 = new ListNodeWithRandom(3) { next = node2, random = node1};
            var node4 = new ListNodeWithRandom(2) { next = node3, random = node3};
            var node5 = new ListNodeWithRandom(1) { next = node4, random = node2};
            node1.random = node5;
            node2.random = node4;

            // (1, 4) -> (2, 3) -> (3, 5) -> (4, 2) -> (5, 1)
            return node5;
        }
    }
}
