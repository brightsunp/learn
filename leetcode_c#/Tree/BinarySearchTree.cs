/**
* Binary search tree is classified on the basis of node values:
*   1. The left subtree of a node contains only nodes with keys less than the node's key. 
*   2. The right subtree of a node contains only nodes with keys greater than the node's key. 
*   3. The left and right subtree each must also be a binary search tree.
*/
using System.Collections.Generic;
using TestMain.Definitions;
using TestMain.Snippets;

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

            AssertTrue(IsValieBSTInorderIterative(TreeNode.SampleBST()));
            AssertTrue(!IsValieBSTInorderIterative(TreeNode.Sample()));

            var inorder = new int[] { 1, 2, 3, 4, 5, 6, 7 };
            AssertEqual(inorder, SortedArrayToBST(inorder).InOrder());
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

        private bool IsValieBSTInorderIterative(TreeNode root)
        {
            var stack = new Stack<TreeNode>();
            TreeNode pre = null;
            TreeNode cur = root;
            while (cur != null || stack.Count > 0)
            {
                if (cur != null)
                {
                    stack.Push(cur);
                    cur = cur.left;
                }
                else
                {
                    cur = stack.Pop();
                    if (pre != null && pre.val >= cur.val)
                    {
                        return false;
                    }
                    pre = cur;
                    cur = cur.right;
                }
            }
            return true;
        }

        private TreeNode SortedArrayToBST(int[] nums)
        {
            return SortedArrayToBSTHelper(nums, 0, nums.Length - 1);
        }

        private TreeNode SortedArrayToBSTHelper(int[] nums, int start, int end)
        {
            if (start > end)
            {
                return null;
            }
            int mid = (start + end) >> 1;
            var root = new TreeNode(nums[mid])
            {
                left = SortedArrayToBSTHelper(nums, start, mid - 1),
                right = SortedArrayToBSTHelper(nums, mid + 1, end)
            };
            return root;
        }
    }
}
