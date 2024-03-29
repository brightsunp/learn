﻿/**
* Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
* You should preserve the original relative order of the nodes in each of the two partitions.
*/
using TestMain.Definitions;

namespace TestMain.LinkedList
{
    class Partition : Solution
    {
        public override void Run()
        {
            TestOutput(nameof(PartitionInternal), PartitionInternal(ListNode.Sample(), 4));
            TestOutput(nameof(PartitionInternal), PartitionInternal(ListNode.SampleIntersect(), 4));
        }

        private ListNode PartitionInternal(ListNode head, int x)
        {
            var dummyA = new ListNode(0);
            var dummyB = new ListNode(0);
            ListNode preA = dummyA, preB = dummyB;
            while (head != null)
            {
                if (head.val < x)
                {
                    preA.next = head;
                    preA = preA.next;
                }
                else
                {
                    preB.next = head;
                    preB = preB.next;
                }
                head = head.next;
            }
            // This is something subtle but key. (e.g. 1 -> 3 -> 5 -> 2, 2)
            preA.next = dummyB.next;
            preB.next = null;

            return dummyA.next;
        }
    }
}
