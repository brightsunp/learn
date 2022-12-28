using TestMain.Definitions;

namespace TestMain.Snippets
{
    static class LinkedList
    {
        public static ListNode Reverse(this ListNode head, ListNode end = null)
        {
            ListNode newHead = end;
            while (head != end)
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
