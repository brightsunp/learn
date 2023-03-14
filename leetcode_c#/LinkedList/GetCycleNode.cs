/**
* Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
* There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
* Do not modify the linked list.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class GetCycleNode : Solution
    {
        public override void Run()
        {
            AssertNull(GetCycleInternal(ListNode.Sample()));
            TestOutput(nameof(GetCycleInternal), GetCycleInternal(ListNode.SampleCycle()));
        }

        // 1. Judge if there is cycle, return the meeting node "tail"
        // 2. Get intersection node of [head -> ... -> tail] and [tail.next -> ... -> tail]
        private ListNode GetCycleInternal(ListNode head)
        {
            ListNode slow = head, fast = head;
            bool isCycle = false;
            while (fast != null && fast.next != null)
            {
                slow = slow.next;
                fast = fast.next.next;
                if (slow == fast)
                {
                    isCycle = true;
                    break;
                }
            }
            if (!isCycle)
            {
                return null;
            }

            int lenA = 1;
            ListNode curA = head;
            while (curA != slow)
            {
                curA = curA.next;
                lenA++;
            }
            int lenB = 1;
            ListNode curB = slow.next;
            while (curB != slow)
            {
                curB = curB.next;
                lenB++;
            }
            curA = head;
            curB = slow.next;
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
            while (curA != curB)
            {
                curA = curA.next;
                curB = curB.next;
            }
            return curA;
        }
    }
}
