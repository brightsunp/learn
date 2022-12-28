/**
* TestMain entry.
*/
using TestMain.LinkedList;

namespace TestMain
{
    class Program
    {
        static void Main(string[] args)
        {
            TestLinkedList();
        }

        private static void TestLinkedList()
        {
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
