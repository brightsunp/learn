/**
 * Definition for a binary tree node.
 */

namespace TestMain.Definitions
{
    public class TreeNode
    {
        public int val;
        public TreeNode left;
        public TreeNode right;

        public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null)
        {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        public static TreeNode Sample()
        {
            var leftNode = new TreeNode(2, new TreeNode(4), new TreeNode(5));
            var rightNode = new TreeNode(3, new TreeNode(6), new TreeNode(7));
            var root = new TreeNode(1, leftNode, rightNode);

            //       1
            //     /   \
            //   2      3
            //  / \    / \
            // 4   5  6   7
            return root;
        }

        public static TreeNode SampleNotPerfect()
        {
            var leftNode = new TreeNode(2, null, new TreeNode(5));
            var rightNode = new TreeNode(3, new TreeNode(6), null);
            var root = new TreeNode(1, leftNode, rightNode);

            //       1
            //     /   \
            //   2      3
            //    \    / 
            //     5  6   
            return root;
        }

        public static TreeNode SampleBST()
        {
            var leftNode = new TreeNode(2, new TreeNode(1), new TreeNode(3));
            var rightNode = new TreeNode(6, new TreeNode(5), new TreeNode(7));
            var root = new TreeNode(4, leftNode, rightNode);

            //       4
            //     /   \
            //   2      6
            //  / \    / \
            // 1   3  5   7
            return root;
        }
    }
}
