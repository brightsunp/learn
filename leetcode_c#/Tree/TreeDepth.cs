/**
* Depth: 
*   1. Depth of a node is the distance from that node to the deepest node of that subtree. 
*   2. Depth/Height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node. 
* 
* Most of the problems can be solved with Depth First Search recursion.
*/
using System.Collections.Generic;
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
            
            AssertEqual(new string[] { "1->2->4", "1->2->5", "1->3->6", "1->3->7" }, FindAllPaths(actual));
            AssertEqual(new int[] { 6, 3, 2, 1, 5, 0 }, ConstructMaximumBinaryTreeNaive(new int[] { 3, 2, 1, 6, 0, 5 }).PreOrder());
            AssertEqual(new int[] { 6, 3, 2, 1, 5, 0 }, ConstructMaximumBinaryTreeLinearTime(new int[] { 3, 2, 1, 6, 0, 5 }).PreOrder());
        }

        // Lowest Common Ancestor: the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).
        // The number of nodes is in the range [2, 10^5]; All Node.val are unique; p != q; p and q will exist in the tree.
        private TreeNode FindLCA(TreeNode root, TreeNode p, TreeNode q)
        {
            if (root == null) return null;

            // Find itself as ancestor.
            if (root.val == p.val || root.val == q.val) return root;
            TreeNode leftLCA = FindLCA(root.left, p, q), rightLCA = FindLCA(root.right, p, q);

            // If can be found in both left subtree and right subtree, root is LCA.
            if (leftLCA != null && rightLCA != null) return root;

            // If cannot be found in left subtree, LCA must be in right subtree; vice versa.
            return leftLCA ?? rightLCA;
        }

        // Given the root of a binary tree, return all root-to-leaf paths in any order.
        private IList<string> FindAllPaths(TreeNode root)
        {
            var paths = new List<string>();
            FindAllPathsHelper(root, new List<int>(), paths);
            return paths;
        }

        private void FindAllPathsHelper(TreeNode root, IList<int> path, IList<string> paths)
        {
            if (root == null) return;

            path.Add(root.val);
            if (root.left == null && root.right == null)
            {
                paths.Add(string.Join("->", path));
            }
            else
            {
                FindAllPathsHelper(root.left, path, paths);
                FindAllPathsHelper(root.right, path, paths);
            }
            path.RemoveAt(path.Count - 1);
        }

        // Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum.
        // Each path should be returned as a list of the node values, not node references.
        private IList<IList<int>> PathSum(TreeNode root, int targetSum)
        {
            var paths = new List<IList<int>>();
            PathSumHelper(root, targetSum, new List<int>(), paths);
            return paths;
        }

        private void PathSumHelper(TreeNode root, int targetSum, IList<int> path, IList<IList<int>> paths)
        {
            if (root == null) return;

            path.Add(root.val);
            if (root.left == null && root.right == null)
            {
                if (targetSum == root.val) paths.Add(new List<int>(path));
            }
            else
            {
                PathSumHelper(root.left, targetSum - root.val, path, paths);
                PathSumHelper(root.right, targetSum - root.val, path, paths);
            }
            path.RemoveAt(path.Count - 1);
        }

        // You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:
        //  1. Create a root node whose value is the maximum value in nums.
        //  2. Recursively build the left subtree on the subarray prefix to the left of the maximum value.
        //  3. Recursively build the right subtree on the subarray suffix to the right of the maximum value.
        //  4. Return the maximum binary tree built from nums.
        private TreeNode ConstructMaximumBinaryTreeNaive(int[] nums)
        {
            return ConstrutHelper(nums, 0, nums.Length - 1);
        }

        private TreeNode ConstrutHelper(int[] nums, int lo, int hi)
        {
            if (lo > hi) return null;

            int pos = FindMaxNumIndex(nums, lo, hi);
            return new TreeNode(nums[pos])
            {
                left = ConstrutHelper(nums, lo, pos - 1),
                right = ConstrutHelper(nums, pos + 1, hi)
            };
        }

        private int FindMaxNumIndex(int[] nums, int lo, int hi)
        {
            int res = lo;
            for (int i = lo; i <= hi; i++)
            {
                if (nums[i] > nums[res])
                {
                    res = i;
                }
            }
            return res;
        }

        // Magic of monotonous stack!
        private TreeNode ConstructMaximumBinaryTreeLinearTime(int[] nums)
        {
            if (nums.Length == 0) return null;

            var stack = new Stack<TreeNode>();
            foreach (int num in nums)
            {
                var cur = new TreeNode(num);
                while (stack.Count > 0 && stack.Peek().val < num)
                {
                    // Temporarily, the relationship may change in future.
                    cur.left = stack.Pop();
                }
                if (stack.Count > 0)
                {
                    stack.Peek().right = cur;
                }
                stack.Push(cur);
            }
            while (stack.Count > 1)
            {
                stack.Pop();
            }
            return stack.Peek();
        }
    }
}
