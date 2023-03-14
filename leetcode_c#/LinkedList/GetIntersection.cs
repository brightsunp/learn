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
            TestOutput(nameof(GetIntersectionInternal), GetIntersectionInternal(ListNode.Sample(), ListNode.SampleIntersect()));
        }

        private ListNode GetIntersectionInternal(ListNode headA, ListNode headB)
        {
            if (headA == null || headB == null)
            {
                return null;
            }

            int lenA = 1;
            ListNode curA = headA;
            while (curA != null && curA.next != null)
            {
                curA = curA.next;
                lenA++;
            }

            int lenB = 1;
            ListNode curB = headB;
            while (curB != null && curB.next != null)
            {
                curB = curB.next;
                lenB++;
            }

            // Last node must be the same
            if (curA.val != curB.val)
            {
                return null;
            }

            // Let longer list move (m-n) first
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
