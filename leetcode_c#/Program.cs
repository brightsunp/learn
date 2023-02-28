/**
* TestMain entry.
*/
using TestMain.Backtracking;
using TestMain.Bitwise;
using TestMain.DynamicProgramming;
using TestMain.Greedy;
using TestMain.LinkedList;
using TestMain.Search;
using TestMain.Sort;
using TestMain.StackAndQueue;
using TestMain.Tree;

namespace TestMain
{
    class Program
    {
        static void Main(string[] args)
        {
            TestGreedy();
            TestDp();
            TestBitwise();
            //TestBacktracking();
            TestTree();
            TestSearch();
            TestSort();
            TestStackAndQueue();
            TestLinkedList();
        }

        private static void TestGreedy()
        {
            var mergeIntervals = new MergeIntervals();
            mergeIntervals.Run();

            var jumpGame = new JumpGame();
            jumpGame.Run();

            var threeSum = new ThreeSum();
            threeSum.Run();

            var removeKdigits = new RemoveKdigits();
            removeKdigits.Run();

            var lemonade = new LemonadeChange();
            lemonade.Run();

            var cookies = new AssignCookies();
            cookies.Run();
        }

        private static void TestDp()
        {
            var intBreak = new IntegerBreak();
            intBreak.Run();

            var triangle = new TrianglePathSum();
            triangle.Run();

            var squares = new PerfectSquares();
            squares.Run();

            var robSeries = new HouseRobberSeries();
            robSeries.Run();

            var wiggle = new WiggleSubsequence();
            wiggle.Run();

            var stockSeries = new StockSeries();
            stockSeries.Run();

            var coinSeries = new CoinChangeSeries();
            coinSeries.Run();

            var partition = new PartitionEqualSum();
            partition.Run();

            var lps = new LongestPalindromeSubsequence();
            lps.Run();

            var lis = new LongestIncreasingSubsequence();
            lis.Run();

            var maxSubarray = new MaxSubarray();
            maxSubarray.Run();

            var uniquePaths = new UniquePaths();
            uniquePaths.Run();

            var fibSeries = new FibonacciSeries();
            fibSeries.Run();
        }

        private static void TestBitwise()
        {
            var maxProduct = new MaxProduct();
            maxProduct.Run();

            var singleNumber = new SingleNumbers();
            singleNumber.Run();

            var bitMain = new BitwiseMain();
            bitMain.Run();
        }

        private static void TestBacktracking()
        {
            var parenthesis = new GenerateParenthesis();
            parenthesis.Run();

            var backtracking = new RecursiveBacktracking();
            backtracking.Run();
        }

        private static void TestTree()
        {
            var bst = new BinarySearchTree();
            bst.Run();

            var heap = new HeapMain();
            heap.Run();

            var treeMain = new TreeMain();
            treeMain.Run();
        }

        private static void TestSearch()
        {
            var findPeak = new FindPeakElement();
            findPeak.Run();

            var matrix = new SearchMatrix();
            matrix.Run();

            var median = new MedianOfTwoSorted();
            median.Run();

            var binary = new BinarySearch();
            binary.Run();

            var rotated = new SearchRotated();
            rotated.Run();
        }

        private static void TestSort()
        {
            var twoSum = new TwoSum();
            twoSum.Run();

            var mergeK = new MergeKLists();
            mergeK.Run();

            var count = new CountSmaller();
            count.Run();

            var sortColors = new SortColors();
            sortColors.Run();

            var merge = new MergeSortedArray();
            merge.Run();

            var sortMain = new SortMain();
            sortMain.Run();
        }

        private static void TestStackAndQueue()
        {
            var maxWindow = new MaxSlidingWindow();
            maxWindow.Run();

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
