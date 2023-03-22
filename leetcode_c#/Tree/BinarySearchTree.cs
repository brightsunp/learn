﻿/**
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
            AssertTrue(IsValidBSTRecursive(TreeNode.SampleBST()));
            AssertTrue(!IsValidBSTRecursive(TreeNode.Sample()));

            AssertTrue(IsValidBSTInorder(TreeNode.SampleBST()));
            AssertTrue(!IsValidBSTInorder(TreeNode.Sample()));

            AssertTrue(IsValieBSTInorderIterative(TreeNode.SampleBST()));
            AssertTrue(!IsValieBSTInorderIterative(TreeNode.Sample()));

            var inorder = new int[] { 1, 2, 3, 4, 5, 6, 7 };
            AssertEqual(inorder, SortedArrayToBST(inorder).InOrder());
        }

        // Given the root of a binary tree, determine if it is a valid BST.
        private bool IsValidBSTRecursive(TreeNode root)
        {
            // Do not use int.MaxValue/MinValue since node.val can be equal to them.
            return IsValidBSTHelper(root, null, null);
        }

        private bool IsValidBSTHelper(TreeNode node, TreeNode lo, TreeNode hi)
        {
            if (node == null) return true;

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
                if (values[i] <= values[i - 1]) return false;
            }
            return true;
        }

        private void IsValidBSTInorderHelper(TreeNode node, List<int> values)
        {
            if (node == null) return;

            IsValidBSTInorderHelper(node.left, values);
            values.Add(node.val);
            IsValidBSTInorderHelper(node.right, values);
        }

        private bool IsValieBSTInorderIterative(TreeNode root)
        {
            var stack = new Stack<TreeNode>();
            TreeNode pre = null, cur = root;
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
                    if (pre != null && pre.val >= cur.val) return false;
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
            if (start > end) return null;

            int mid = (start + end) >> 1;
            return new TreeNode(nums[mid])
            {
                left = SortedArrayToBSTHelper(nums, start, mid - 1),
                right = SortedArrayToBSTHelper(nums, mid + 1, end)
            };
        }

        // It is much more tricky to find LCA in BST: "leftLCA ?? rightLCA" can be simply translated.
        private TreeNode FindLcaInBST(TreeNode root, TreeNode p, TreeNode q)
        {
            if (root == null) return null;

            if (root.val > p.val && root.val > q.val) return FindLcaInBST(root.left, p, q);
            if (root.val < p.val && root.val < q.val) return FindLcaInBST(root.right, p, q);
            return root;
        }

        // Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
        //  1. Search for a node to remove.
        //  2. If the node is found, delete the node.
        private TreeNode DeleteNode(TreeNode root, int key)
        {
            TreeNode pre = null, cur = root;
            while (cur != null && cur.val != key)
            {
                pre = cur;
                if (cur.val > key)
                {
                    cur = cur.left;
                }
                else
                {
                    cur = cur.right;
                }
            }

            // Find target at root, or never find target.
            if (pre == null) return DeleteThisNode(cur);
            if (pre.left == cur)
            {
                pre.left = DeleteThisNode(cur);
            }
            else
            {
                pre.right = DeleteThisNode(cur);
            }
            return root;
        }

        private TreeNode DeleteThisNode(TreeNode root)
        {
            if (root == null) return null;
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;

            // Find leftmost successor (min node) in right subtree.
            TreeNode pre = root, cur = root.right;
            while (cur.left != null)
            {
                pre = cur;
                cur = cur.left;
            }

            // Delete min node.
            if (pre != root)
            {
                pre.left = cur.right;
            }
            else
            {
                pre.right = cur.right;
            }

            // Replace root val with min val.
            root.val = cur.val;
            return root;
        }
    }
}
