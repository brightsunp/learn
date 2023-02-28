/**
* A valid binary search tree is defined as follows: 
* 1. The left subtree of a node contains only nodes with keys less than the node's key. 
* 2. The right subtree of a node contains only nodes with keys greater than the node's key. 
* 3. Both the left and right subtrees must also be binary search trees.
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Tree
{
    class BinarySearchTree : Solution
    {
        public override void Run()
        {
            AssertTrue(IsValidBST(TreeNode.SampleBST()));
            AssertTrue(!IsValidBST(TreeNode.Sample()));

            AssertTrue(IsValidBSTInorder(TreeNode.SampleBST()));
            AssertTrue(!IsValidBSTInorder(TreeNode.Sample()));
        }

        // Given the root of a binary tree, determine if it is a valid BST.
        private bool IsValidBST(TreeNode root)
        {
            // Do not use int.MaxValue/MinValue since node.val can be equal to them.
            return IsValidBSTHelper(root, null, null);
        }

        private bool IsValidBSTHelper(TreeNode node, TreeNode lo, TreeNode hi)
        {
            if (node == null)
            {
                return true;
            }

            // This makes sure grandchildren are also compared with the ancestor.
            if ((lo != null && node.val <= lo.val) || (hi != null && node.val >= hi.val))
            {
                return false;
            }
            return IsValidBSTHelper(node.left, lo, node) && IsValidBSTHelper(node.right, node, hi);
        }

        private bool IsValidBSTInorder(TreeNode root)
        {
            // Inorder traversal returns an array in ascending order.
            var values = new List<int>();
            IsValidBSTInorderHelper(root, values);

            for(int i = 1; i < values.Count; i++)
            {
                if (values[i] <= values[i - 1])
                {
                    return false;
                }
            }
            return true;
        }

        private void IsValidBSTInorderHelper(TreeNode node, List<int> values)
        {
            if (node == null)
            {
                return;
            }

            IsValidBSTInorderHelper(node.left, values);
            values.Add(node.val);
            IsValidBSTInorderHelper(node.right, values);
        }
    }
}
