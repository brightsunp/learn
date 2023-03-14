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
            TestOutput(nameof(CopyRandomListInternal), CopyRandomListInternal(ListNodeWithRandom.Sample()));
        }

        // Loop 1: replicate each node (like DNA)
        // Loop 2: assign random pointer for each duplicated node
        // Loop 3: extract the replicate and restore the original list
        private ListNodeWithRandom CopyRandomListInternal(ListNodeWithRandom head)
        {
            ListNodeWithRandom cur = head;
            while (cur != null)
            {
                ListNodeWithRandom tmp = cur.next;
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

            cur = head;
            var dummy = new ListNodeWithRandom(0);
            ListNodeWithRandom curNew = dummy;
            while (cur != null)
            {
                ListNodeWithRandom tmp = cur.next.next;
                ListNodeWithRandom copy = cur.next;
                curNew.next = copy;
                curNew = curNew.next;

                cur.next = tmp;
                cur = cur.next;
            }

            return dummy.next;
        }
    }
}
