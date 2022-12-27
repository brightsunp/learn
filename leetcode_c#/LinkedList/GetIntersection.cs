/**
* Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
* If the two linked lists have no intersection at all, return null.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class GetIntersection : Solution
    {
        public override void Run()
        {
            var test1 = ListNode.Sample();
            var test2 = ListNode.SampleIntersect();
            TestOutput(nameof(GetIntersectionInternal), GetIntersectionInternal(test1, test2));
        }

        // Last node must be the same; let longer list move (m-n) first
        private ListNode GetIntersectionInternal(ListNode headA, ListNode headB)
        {
            if (headA == null || headB == null)
            {
                return null;
            }

            int lenA = 1;
            var curA = headA;
            while (curA != null && curA.next != null)
            {
                curA = curA.next;
                lenA++;
            }

            int lenB = 1;
            var curB = headB;
            while (curB != null && curB.next != null)
            {
                curB = curB.next;
                lenB++;
            }

            if (curA.val != curB.val)
            {
                return null;
            }

            curA = headA;
            curB = headB;
            while (lenA > lenB)
            {
                curA = curA.next;
                lenA--;
            }
            while (lenB > lenA)
            {
                curB = curB.next;
                lenB--;
            }

            while (curA != null)
            {
                if (curA.val == curB.val)
                {
                    return curA;
                }

                curA = curA.next;
                curB = curB.next;
            }

            return null;
        }
    }
}
