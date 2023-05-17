/**
* You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
*   I. Adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. 
*   II. All houses at this place are arranged in a circle. Plus constraint I. 
*   III. All houses in this place form a binary tree, and there is only one entrance called root. "if two directly-linked houses were broken into on the same night."
* 
* Given an integer array (or root node) representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
* 1 <= nums.length <= 100, 0 <= nums[i] <= 400
*/
using System;
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.DynamicProgramming
{
    class HouseRobberSeries : Solution
    {
        public override void Run()
        {
            AssertEqual(4, RobNaive(new int[] { 1, 2, 3, 1 }));
            AssertEqual(12, RobNaive(new int[] { 2, 7, 9, 3, 1 }));
            AssertEqual(4, RobConstant(new int[] { 1, 2, 3, 1 }));
            AssertEqual(12, RobConstant(new int[] { 2, 7, 9, 3, 1 }));

            AssertEqual(3, RobII(new int[] { 2, 3, 2 }));
            AssertEqual(4, RobII(new int[] { 1, 2, 3, 1 }));
            AssertEqual(3, RobII(new int[] { 1, 2, 3 }));

            AssertEqual(23, RobIIIRecursiveNaive(TreeNode.Sample()));
            AssertEqual(23, RobIIIRecursiveDp(TreeNode.Sample()));
            AssertEqual(23, RobIIIGreedy(TreeNode.Sample()));
        }

        private int RobNaive(int[] nums)
        {
            var dp = new int[nums.Length + 1];
            dp[1] = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                dp[i + 1] = Math.Max(dp[i], dp[i - 1] + nums[i]);
            }
            return dp[nums.Length];
        }

        private int RobConstant(int[] nums)
        {
            int pre = 0, cur = nums[0];
            for (int i = 1; i < nums.Length; i++)
            {
                int tmp = cur;
                cur = Math.Max(cur, pre + nums[i]);
                pre = tmp;
            }
            return cur;
        }

        // Divide the problem into 2 sub-problems: sequences with or without nums[0].
        private int RobII(int[] nums)
        {
            if (nums.Length == 1)
            {
                return nums[0];
            }

            int pre1 = nums[0], cur1 = Math.Max(nums[0], nums[1]), pre2 = 0, cur2 = nums[1];
            for (int i = 2; i < nums.Length; i++)
            {
                if (i == nums.Length - 1)
                {
                    cur2 = Math.Max(cur2, pre2 + nums[i]);
                }
                else
                {
                    int tmp1 = cur1, tmp2 = cur2;
                    cur1 = Math.Max(cur1, pre1 + nums[i]);
                    cur2 = Math.Max(cur2, pre2 + nums[i]);
                    pre1 = tmp1;
                    pre2 = tmp2;
                }
            }
            return Math.Max(cur1, cur2);
        }

        // Get the recursive solution from naive thinking.
        private int RobIIIRecursiveNaive(TreeNode root)
        {
            if (root == null)
            {
                return 0;
            }

            int res = root.val;
            if (root.left != null)
            {
                res += RobIIIRecursiveNaive(root.left.left) + RobIIIRecursiveNaive(root.left.right);
            }
            if (root.right != null)
            {
                res += RobIIIRecursiveNaive(root.right.left) + RobIIIRecursiveNaive(root.right.right);
            }
            return Math.Max(res, RobIIIRecursiveNaive(root.left) + RobIIIRecursiveNaive(root.right));
        }

        // Improve efficiency with DP mind.
        private int RobIIIRecursiveDp(TreeNode root)
        {
            return RobIIIHelper(root, new Dictionary<TreeNode, int>());
        }

        private int RobIIIHelper(TreeNode root, Dictionary<TreeNode, int> cache)
        {
            if (root == null)
            {
                return 0;
            }
            if (cache.ContainsKey(root))
            {
                return cache[root];
            }

            int res = root.val;
            if (root.left != null)
            {
                res += RobIIIHelper(root.left.left, cache) + RobIIIHelper(root.left.right, cache);
            }
            if (root.right != null)
            {
                res += RobIIIHelper(root.right.left, cache) + RobIIIHelper(root.right.right, cache);
            }
            res = Math.Max(res, RobIIIHelper(root.left, cache) + RobIIIHelper(root.right, cache));
            cache.Add(root, res);
            return res;
        }

        // Each step: choose to rob the node or not.
        private int RobIIIGreedy(TreeNode root)
        {
            int[] res = RobIIIGreedyHelper(root);
            return Math.Max(res[0], res[1]);
        }

        private int[] RobIIIGreedyHelper(TreeNode root)
        {
            if (root == null)
            {
                return new int[2];
            }

            int[] left = RobIIIGreedyHelper(root.left);
            int[] right = RobIIIGreedyHelper(root.right);
            var res = new int[2];
            // res[0] is the max result NOT robbing the node, which means both child nodes can be robbed.
            res[0] = Math.Max(left[0], left[1]) + Math.Max(right[0], right[1]);
            // res[1] is the max result robbing the node, which means NOT robbing any child node.
            res[1] = root.val + left[0] + right[0];
            return res;
        }
    }
}
