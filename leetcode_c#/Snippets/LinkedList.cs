using TestMain.Definitions;

namespace TestMain.Snippets
{
    static class LinkedList
    {
        public static ListNode Reverse(this ListNode head)
        {
            ListNode newHead = null;
            while (head != null)
            {
                var tmp = head.next;
                head.next = newHead;
                newHead = head;
                head = tmp;
            }

            return newHead;
        }
    }
}
