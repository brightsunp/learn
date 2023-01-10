/**
* Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
* 
* Implement all the functions:
* 1. void push(int val) pushes the element val onto the stack.
* 2. void pop() removes the element on the top of the stack.
* 3. int top() gets the top element of the stack.
* 4. int getMin() retrieves the minimum element in the stack.
* 
* You must implement a solution with O(1) time complexity for each function.
*/
using TestMain.Definitions;
using System.Collections.Generic;

namespace TestMain.StackAndQueue
{
    class MinStack : Solution
    {
        private Stack<int> allValues = new Stack<int>();
        private int minValue = int.MaxValue;
        private Node head = null;

        public override void Run()
        {
            MinStack minStack = new MinStack();

            minStack.Push(-2);
            minStack.Push(0);
            minStack.Push(-3);
            AssertEqual(-3, minStack.GetMin());
            minStack.Pop();
            AssertEqual(0, minStack.Top());
            AssertEqual(-2, minStack.GetMin());

            minStack.PushNode(-2);
            minStack.PushNode(0);
            minStack.PushNode(-3);
            AssertEqual(-3, minStack.GetMinNode());
            minStack.PopNode();
            AssertEqual(0, minStack.TopNode());
            AssertEqual(-2, minStack.GetMinNode());
        }

        public void Push(int val)
        {
            // Maintain the order that minimum value is always followed by second minimum value
            if (val <= minValue)
            {
                allValues.Push(minValue);
                minValue = val;
            }
            allValues.Push(val);
        }

        public void Pop()
        {
            int top = allValues.Pop();
            if (top == minValue)
            {
                minValue = allValues.Pop();
            }
        }

        public int Top()
        {
            return allValues.Peek();
        }

        public int GetMin()
        {
            return minValue;
        }

        public void PushNode(int val)
        {
            if (head == null)
            {
                head = new Node(val, val, null);
            }
            else
            {
                head = new Node(val, System.Math.Min(val, head.min), head);
            }
        }

        public void PopNode()
        {
            head = head.next;
        }

        public int TopNode()
        {
            return head.val;
        }

        public int GetMinNode()
        {
            return head.min;
        }
    }

    class Node
    {
        public int val;
        public int min;
        public Node next;

        public Node(int val, int min, Node next)
        {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
}
