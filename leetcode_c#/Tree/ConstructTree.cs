/**
* Given two integer arrays which are preorder traversal and inorder traversal of the same tree. 
* Construct and return the binary tree.
* 
* 1 <= preorder.length <= 3000, inorder.length == preorder.length, preorder and inorder consist of unique values.
*/
using System.Collections.Generic;
using TestMain.Definitions;
using TestMain.Snippets;

namespace TestMain.Tree
{
    class ConstructTree : Solution
    {
        public override void Run()
        {
            var preorder = new int[] { 1, 2, 4, 5, 3, 6, 7 };
            var inorder = new int[] { 4, 2, 5, 1, 6, 3, 7 };
            TreeNode actual = BuildTreeRecursive(preorder, inorder);
            AssertEqual(preorder, actual.PreOrder());
            AssertEqual(inorder, actual.InOrder());

            actual = BuildTree(preorder, inorder);
            AssertEqual(preorder, actual.PreOrder());
            AssertEqual(inorder, actual.InOrder());
        }

        private TreeNode BuildTreeRecursive(int[] preorder, int[] inorder)
        {
            if (preorder.Length == 0)
            {
                return null;
            }
            
            int pos = System.Array.IndexOf(inorder, preorder[0]);
            int leftCount = pos, rightCount = inorder.Length - pos - 1;
            var root = new TreeNode(preorder[0])
            {
                left = BuildTreeRecursive(new List<int>(preorder).GetRange(1, leftCount).ToArray(), new List<int>(inorder).GetRange(0, leftCount).ToArray()),
                right = BuildTreeRecursive(new List<int>(preorder).GetRange(pos + 1, rightCount).ToArray(), new List<int>(inorder).GetRange(pos + 1, rightCount).ToArray())
            };
            return root;
        }

        private TreeNode BuildTree(int[] preorder, int[] inorder)
        {
            var indexMap = new Dictionary<int, int>();
            for (int i = 0; i < inorder.Length; i++)
            {
                indexMap.Add(inorder[i], i);
            }
            return BuildTreeHelper(preorder, inorder, indexMap, 0, 0, inorder.Length - 1);
        }

        private TreeNode BuildTreeHelper(int[] preorder, int[] inorder, Dictionary<int, int> indexMap, int preStart, int inStart, int inEnd)
        {
            // preStart > preEnd || inStart > inEnd
            if (preStart > preorder.Length - 1 || inStart > inEnd)
            {
                return null;
            }
            
            int inIndex = indexMap[preorder[preStart]];
            var root = new TreeNode(preorder[preStart])
            {
                left = BuildTreeHelper(preorder, inorder, indexMap, preStart + 1, inStart, inIndex - 1),
                right = BuildTreeHelper(preorder, inorder, indexMap, preStart + inIndex - inStart + 1, inIndex + 1, inEnd)
            };
            return root;
        }
    }
}
