/**
* Recursive traversal implementation are corresponding to how the tree is traversed.
*   pre-order: print(val) / pre-recursive(left) / pre-recursive(right)
*       Duplicate tree / Prefix expression tree
*   in-oder: in-recursive(left) / print(val) / in-recursive(right)
*       Binary search tree
*   post-order: post-recursive(left) / post-recursive(right) / print(val)
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
            if (root == null)
            {
                return res;
            }

            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count != 0)
            {
                var levelRes = new List<int>();
                int levelCount = queue.Count;
                while (levelCount > 0)
                {
                    TreeNode cur = queue.Dequeue();
                    levelRes.Add(cur.val);
                    if (cur.left != null)
                    {
                        queue.Enqueue(cur.left);
                    }
                    if (cur.right != null)
                    {
                        queue.Enqueue(cur.right);
                    }
                    levelCount--;
                }
                res.Add(levelRes);
            }

            return res;
        }

        // Leverage FILO stack: root -> left subtree -> right subtree.
        public static IList<int> PreOrder(this TreeNode root)
        {
            var res = new List<int>();
            if (root == null)
            {
                return res;
            }

            var stack = new Stack<TreeNode>();
            stack.Push(root);
            while (stack.Count != 0)
            {
                TreeNode cur = stack.Pop();
                res.Add(cur.val);
                if (cur.right != null)
                {
                    stack.Push(cur.right);
                }
                if (cur.left != null)
                {
                    stack.Push(cur.left);
                }
            }

            return res;
        }

        // Leverage FILO stack: left subtree -> root -> right subtree.
        public static IList<int> InOrder(this TreeNode root)
        {
            var res = new List<int>();
            var stack = new Stack<TreeNode>();

            // This way root is not modified.
            TreeNode cur = root;
            while (cur != null || stack.Count != 0)
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

        // Leverage FILO stack: left subtree -> right subtree -> root. (*Reverse the print step of pre-order)
        public static IList<int> PostOrder(this TreeNode root)
        {
            var res = new List<int>();
            if (root == null)
            {
                return res;
            }

            var stack = new Stack<TreeNode>();
            stack.Push(root);
            while (stack.Count != 0)
            {
                TreeNode cur = stack.Pop();
                
                // Since each element is added at the start, we also need to reverse the order popping children nodes.
                res.Insert(0, cur.val);
                if (cur.left != null)
                {
                    stack.Push(cur.left);
                }
                if (cur.right != null)
                {
                    stack.Push(cur.right);
                }
            }

            return res;
        }

        // Recursive using Depth First Search, or iterative using Breadth First Search (level order traversal).
        public static int MaxDepth(this TreeNode root)
        {
            if (root == null)
            {
                return 0;
            }

            int lMaxDepth = MaxDepth(root.left);
            int rMaxDepth = MaxDepth(root.right);
            return Math.Max(lMaxDepth, rMaxDepth) + 1;
        }

        public static int MinDepth(this TreeNode root)
        {
            if (root == null)
            {
                return 0;
            }

            int lMinDepth = MinDepth(root.left);
            int rMinDepth = MinDepth(root.right);
            if (lMinDepth == 0 || rMinDepth == 0)
            {
                return lMinDepth + rMinDepth + 1;
            }
            return Math.Min(lMinDepth, rMinDepth) + 1;
        }
    }
}
