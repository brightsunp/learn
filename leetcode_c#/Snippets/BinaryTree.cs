﻿/**
* Recursive traversal implementation is corresponding to the print order of root nodes.
*   1. pre-order: print(val) / pre-recursive(left) / pre-recursive(right)
*       Duplicate tree / Prefix expression tree
*   2. in-oder: in-recursive(left) / print(val) / in-recursive(right)
*       Binary search tree
*   3. post-order: post-recursive(left) / post-recursive(right) / print(val)
*       Delete tree / Postfix expression tree
*/
using System;
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Snippets
{
    static class BinaryTree
    {
        // Leverage FIFO queue.
        public static IList<IList<int>> LevelOrder(this TreeNode root)
        {
            var res = new List<IList<int>>();
            if (root == null) return res;

            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count > 0)
            {
                int levelCount = queue.Count;
                var levelRes = new List<int>();
                while (levelCount-- > 0)
                {
                    TreeNode cur = queue.Dequeue();
                    levelRes.Add(cur.val);
                    if (cur.left != null) queue.Enqueue(cur.left);
                    if (cur.right != null) queue.Enqueue(cur.right);
                }
                res.Add(levelRes);
            }
            return res;
        }

        // Leverage LIFO stack: root -> left subtree -> right subtree.
        public static IList<int> PreOrder(this TreeNode root)
        {
            var res = new List<int>();
            if (root == null) return res;

            var stack = new Stack<TreeNode>();
            stack.Push(root);
            while (stack.Count > 0)
            {
                TreeNode cur = stack.Pop();
                res.Add(cur.val);
                if (cur.right != null) stack.Push(cur.right);
                if (cur.left != null) stack.Push(cur.left);
            }
            return res;
        }

        // Leverage LIFO stack: left subtree -> root -> right subtree.
        public static IList<int> InOrder(this TreeNode root)
        {
            var res = new List<int>();
            var stack = new Stack<TreeNode>();
            // No need to check if root == null.
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
                    res.Add(cur.val);
                    cur = cur.right;
                }
            }
            return res;
        }

        // Leverage LIFO stack: left subtree -> right subtree -> root.
        public static IList<int> PostOrder(this TreeNode root)
        {
            var res = new List<int>();
            if (root == null) return res;

            var stack = new Stack<TreeNode>();
            stack.Push(root);
            while (stack.Count > 0)
            {
                TreeNode cur = stack.Pop();
                // Left and right is sequentially unchanged, also need to reverse the order popping children nodes.
                res.Insert(0, cur.val);
                if (cur.left != null) stack.Push(cur.left);
                if (cur.right != null) stack.Push(cur.right);
            }
            return res;
        }

        public static IList<IList<int>> ZigzagLevelOrder(this TreeNode root)
        {
            var res = new List<IList<int>>();
            if (root == null) return res;

            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            bool isLeftToRight = true;
            while (queue.Count > 0)
            {
                int levelCount = queue.Count;
                var levelRes = new int[levelCount];
                for (int i = 0; i < levelCount; i++)
                {
                    TreeNode cur = queue.Dequeue();
                    int index = isLeftToRight ? i : levelCount - 1 - i;
                    levelRes[index] = cur.val;
                    if (cur.left != null) queue.Enqueue(cur.left);
                    if (cur.right != null) queue.Enqueue(cur.right);
                }
                isLeftToRight = !isLeftToRight;
                res.Add(levelRes);
            }
            return res;
        }

        public static int MaxDepth(this TreeNode root)
        {
            if (root == null) return 0;

            return Math.Max(MaxDepth(root.left), MaxDepth(root.right)) + 1;
        }

        public static int MinDepth(this TreeNode root)
        {
            if (root == null) return 0;

            int lMinDepth = MinDepth(root.left);
            int rMinDepth = MinDepth(root.right);
            if (lMinDepth == 0 || rMinDepth == 0)
            {
                // If a node has only one child, MUST return the depth of the side with child.
                return lMinDepth + rMinDepth + 1;
            }
            // If a node has two children, return the min depth of two sides.
            return Math.Min(lMinDepth, rMinDepth) + 1;
        }

        public static int MinDepthBFS(this TreeNode root)
        {
            if (root == null) return 0;

            int res = 1;
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count > 0)
            {
                int levelCount = queue.Count;
                while (levelCount-- > 0)
                {
                    TreeNode cur = queue.Dequeue();
                    if (cur.left == null && cur.right == null) return res;
                    if (cur.left != null) queue.Enqueue(cur.left);
                    if (cur.right != null) queue.Enqueue(cur.right);
                }
                res++;
            }
            return res;
        }

        // Elegant recursive implementation.
        public static int SumOfLeftLeaves(this TreeNode root, bool isLeftChild = false)
        {
            if (root == null) return 0;

            if (root.left == null && root.right == null)
            {
                // Add the value of left leave node.
                return isLeftChild ? root.val : 0;
            }
            return SumOfLeftLeaves(root.left, true) + SumOfLeftLeaves(root.right, false);
        }
    }
}
