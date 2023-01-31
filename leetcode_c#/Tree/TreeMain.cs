/**
* Entry to test all the tree snippets.
*/
using System.Collections.Generic;
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.Tree
{
    class TreeMain : Solution
    {
        public override void Run()
        {
            var actual = TreeNode.Sample();
            var wrapList = new List<List<int>> { new List<int> { 1 }, new List<int> { 2, 3 }, new List<int> { 4, 5, 6, 7 } };
            AssertEqual(wrapList, actual.LevelOrder());

            var expected = new List<int> { 1, 2, 4, 5, 3, 6, 7 };
            AssertEqual(expected, actual.PreOrder());

            expected = new List<int> { 4, 2, 5, 1, 6, 3, 7 };
            AssertEqual(expected, actual.InOrder());

            expected = new List<int> { 4, 5, 2, 6, 7, 3, 1 };
            AssertEqual(expected, actual.PostOrder());

            AssertEqual(3, actual.MaxDepth());
            AssertEqual(3, actual.MinDepth());
        }
    }
}
