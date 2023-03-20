/**
* Depth: 
*   1. Depth of a node is the distance from that node to the deepest node of that subtree. 
*   2. Depth of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node. 
* 
* Most of the problems can be solved with Depth First Search recursion.
*/
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.Tree
{
    class TreeDepth : Solution
    {
        public override void Run()
        {
            TreeNode actual = TreeNode.Sample();
            AssertEqual(3, actual.MaxDepth());
            AssertEqual(3, actual.MinDepth());
            AssertEqual(3, actual.MinDepthBFS());
            AssertEqual(10, actual.SumOfLeftLeaves());
        }
    }
}
