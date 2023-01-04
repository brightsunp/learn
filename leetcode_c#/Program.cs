﻿/**
* TestMain entry.
*/
using TestMain.LinkedList;
using TestMain.Sort;
using TestMain.StackAndQueue;

namespace TestMain
{
    class Program
    {
        static void Main(string[] args)
        {
            TestSort();
            TestStackAndQueue();
            TestLinkedList();
        }

        private static void TestSort()
        {
            var count = new CountSmaller();
            count.Run();

            var sortColors = new SortColors();
            sortColors.Run();

            var merge = new MergeSortedArray();
            merge.Run();

            //var sortMain = new SortMain();
            //sortMain.Run();
        }

        private static void TestStackAndQueue()
        {
            var queue = new MyQueue();
            queue.Run();

            var trap = new TrapRainWater();
            trap.Run();

            var daily = new DailyTemperatures();
            daily.Run();

            var sequence = new StackSequences();
            sequence.Run();

            var minStack = new MinStack();
            minStack.Run();

            var calculator = new BasicCalculator();
            calculator.Run();

            var parentheses = new ValidParentheses();
            parentheses.Run();
        }

        private static void TestLinkedList()
        {
            var copy = new CopyWithRandomPointer();
            copy.Run();

            var reverse2 = new ReverseBetween();
            reverse2.Run();

            var cycle = new GetCycleNode();
            cycle.Run();

            var partition = new Partition();
            partition.Run();

            var mergeTwoSorted = new MergeTwoSorted();
            mergeTwoSorted.Run();

            var intersect = new GetIntersection();
            intersect.Run();

            var reverse = new Reverse();
            reverse.Run();
        }
    }
}
