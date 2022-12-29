/**
* A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
* Construct a deep copy of the list. Return the head of the copied linked list.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class CopyWithRandomPointer : Solution
    {
        public override void Run()
        {
            var test = ListNodeWithRandom.Sample();
            TestOutput(nameof(CopyRandomListInternal), CopyRandomListInternal(test));
        }

        // Loop 1: replicate each node (like DNA)
        // Loop 2: assign random pointer for each duplicated node
        // Loop 3: restore the original and extract the duplicated list
        private ListNodeWithRandom CopyRandomListInternal(ListNodeWithRandom head)
        {
            var cur = head;
            while (cur != null)
            {
                var tmp = cur.next;
                var copy = new ListNodeWithRandom(cur.val);
                cur.next = copy;
                copy.next = tmp;
                cur = tmp;
            }

            cur = head;
            while (cur != null)
            {
                if (cur.random != null)
                {
                    cur.next.random = cur.random.next;
                }
                cur = cur.next.next;
            }

            var dummy = new ListNodeWithRandom(0);
            cur = head;
            var curNew = dummy;
            while (cur != null)
            {
                var tmp = cur.next.next;
                var copy = cur.next;
                curNew.next = copy;
                curNew = copy;

                cur.next = tmp;
                cur = tmp;
            }

            return dummy.next;
        }
    }
}
