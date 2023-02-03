/**
* Min/Max Heap is a special tree-based data structure in which the tree is a complete binary tree.
* 
* It can also be implemented as an array (level order traversal of the complete binary tree): 
*   nums[i].left = nums[2 * i + 1], nums[i].right = nums[2 * i + 2], nums[i].parent = nums[(i - 1) >> 1]
* 
* 1. Heapify: rearrange the elements to maintain the property of heap. O(log N)
* 2. Insertion: insert an element at end, then heapify. O(log N)
* 3. Deletion: replace root element with the last, then delete the last and heapify. O(log N)
* 4. Peek: return root element. O(1)
*/
using System.Collections.Generic;

namespace TestMain.Snippets
{
    // Take MaxHeap as an example
    static class Heap
    {
        public static void InsertNode(this List<int> nums, int newVal)
        {
            nums.Add(newVal);
            int cur = nums.Count - 1;
            while (cur > 0 && nums[ParentIndex(cur)] < nums[cur])
            {
                Swap(nums, ParentIndex(cur), cur);
                cur = ParentIndex(cur);
            }
        }

        public static void DeleteNode(this List<int> nums)
        {
            Swap(nums, 0, nums.Count - 1);
            nums.RemoveAt(nums.Count - 1);
            Heapify(nums, 0);
        }

        public static int Peek(this List<int> nums)
        {
            return nums[0];
        }

        // Heapify a sub-tree taking the given index as the root.
        private static void Heapify(List<int> nums, int i)
        {
            int maxIndex = i, left = LeftChildIndex(i), right = RightChildIndex(i);
            if (left < nums.Count && nums[left] > nums[i])
            {
                maxIndex = left;
            }
            if (right < nums.Count && nums[right] > nums[maxIndex])
            {
                maxIndex = right;
            }
            if (maxIndex != i)
            {
                Swap(nums, i, maxIndex);
                Heapify(nums, maxIndex);
            }
        }

        private static void Swap(List<int> nums, int i, int j)
        {
            int tmp = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
        }

        private static int ParentIndex(int i)
        {
            return (i - 1) >> 1;
        }

        private static int LeftChildIndex(int i)
        {
            return 2 * i + 1;
        }

        private static int RightChildIndex(int i)
        {
            return 2 * i + 2;
        }
    }
}
