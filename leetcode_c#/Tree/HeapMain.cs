/**
* Entry to test heap implementation.
*/
using System.Collections.Generic;
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.Tree
{
    class HeapMain : Solution
    {
        public override void Run()
        {
            var test = new List<int>();
            test.InsertNode(3);
            test.InsertNode(10);
            test.InsertNode(12);
            test.InsertNode(8);
            test.InsertNode(2);
            test.InsertNode(14);

            TestOutput(nameof(HeapMain), $"[{string.Join(",", test)}]");
            AssertEqual(14, test.Peek());

            test.DeleteNode();
            TestOutput(nameof(HeapMain), $"[{string.Join(",", test)}]");
            AssertEqual(12, test.Peek());

            test.InsertNode(15);
            TestOutput(nameof(HeapMain), $"[{string.Join(",", test)}]");
            AssertEqual(15, test.Peek());
        }
    }
}
