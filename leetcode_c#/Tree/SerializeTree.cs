/**
* Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
* or transmitted across a network connection link to be reconstructed later in the same or another computer environment. 
* 
* Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
* You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
* The number of nodes is in [0, 10^4]; -1000 <= Node.val <= 1000
*/
using System.Collections.Generic;
using TestMain.Definitions;

namespace TestMain.Tree
{
    class SerializeTree : Solution
    {
        public override void Run()
        {
            string expected = "1,2,3,#,5,6,#,#,#,#,#";
            AssertEqual(expected, Serialize(TreeNode.SampleNotPerfect()));
            AssertEqual(expected, Serialize(Deserialize(expected)));
        }

        // Encodes the tree to a single string.
        private string Serialize(TreeNode root)
        {
            // Level order traversal: dont't skip null child nodes
            if (root == null)
            {
                return string.Empty;
            }

            var values = new List<string>();
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            while (queue.Count > 0)
            {
                int levelCount = queue.Count;
                while (levelCount-- > 0)
                {
                    TreeNode cur = queue.Dequeue();
                    if (cur != null)
                    {
                        values.Add(cur.val.ToString());
                        queue.Enqueue(cur.left);
                        queue.Enqueue(cur.right);
                    }
                    else
                    {
                        values.Add("#");
                    }
                }
            }
            return string.Join(",", values);
        }

        // Decodes the encoded data to tree.
        private TreeNode Deserialize(string data)
        {
            if (data == string.Empty)
            {
                return null;
            }
            
            string[] values = data.Split(',');
            var root = new TreeNode(System.Convert.ToInt32(values[0]));
            var queue = new Queue<TreeNode>();
            queue.Enqueue(root);
            int i = 1;
            while (i < values.Length)
            {
                TreeNode cur = queue.Dequeue();
                if (values[i] != "#")
                {
                    cur.left = new TreeNode(System.Convert.ToInt32(values[i]));
                    queue.Enqueue(cur.left);
                }
                i++;
                if (values[i] != "#")
                {
                    cur.right = new TreeNode(System.Convert.ToInt32(values[i]));
                    queue.Enqueue(cur.right);
                }
                i++;
            }
            return root;
        }
    }
}
