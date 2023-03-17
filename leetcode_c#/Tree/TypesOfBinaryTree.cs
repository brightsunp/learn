/**
* Types of Binary Tree On the basis of the completion of levels: 
*   1. Complete Binary Tree: all levels are completely filled except possibly the last level, and the last level has all keys as left as possible. 
*   2. Perfect Binary Tree: all levels are completely filled. (all internal nodes have two children and all leaf nodes are at the same level.) 
*   3. Balanced Binary Tree: the height is O(log N) where N is the number of nodes. (the heights of left and right subtrees of every node never differ by more than 1.)
*       - Balanced BST is performance-wise good as it provides O(log N) time for search, insert and delete.
*/
using System;
using TestMain.Definitions;

namespace TestMain.Tree
{
    class TypesOfBinaryTree : Solution
    {
        public override void Run()
        {
            AssertTrue(IsBalancedNaive(TreeNode.Sample()));
            AssertTrue(IsBalancedDp(TreeNode.Sample()));
        }

        // O(n^2) time by the definition of balanced binary tree.
        private bool IsBalancedNaive(TreeNode root)
        {
            if (root == null)
            {
                return true;
            }

            bool res = Math.Abs(Height(root.left) - Height(root.right)) <= 1;
            return res && IsBalancedNaive(root.left) && IsBalancedNaive(root.right);
        }

        private int Height(TreeNode node)
        {
            if (node == null)
            {
                return 0;
            }

            return Math.Max(Height(node.left), Height(node.right)) + 1;
        }

        // O(n) time by the bottom up DP approach.
        private bool IsBalancedDp(TreeNode root)
        {
            return IsBalancedDpHelper(root) != -1;
        }

        private int IsBalancedDpHelper(TreeNode node)
        {
            if (node == null)
            {
                return 0;
            }

            int leftRes = IsBalancedDpHelper(node.left);
            int rightRes = IsBalancedDpHelper(node.right);
            if (leftRes == -1 || rightRes == -1 || Math.Abs(leftRes - rightRes) > 1)
            {
                // Leverage -1 to indicate if balanced or not.
                return -1;
            }

            return Math.Max(leftRes, rightRes) + 1;
        }
    }
}
