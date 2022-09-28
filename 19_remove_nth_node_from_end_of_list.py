# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = self.removeNodeHelper(head, n)
        if count == n + 1:
            head.val = head.next.val
            head.next = head.next.next

        return head

    def removeNodeHelper(self, head: Optional[ListNode], k: int) -> int:
        if head is None:
            return 1
        count = self.removeNodeHelper(head.next, k)
        if count == k + 1:
            head.next = head.next.next

        return count + 1


if __name__ == "__main__":
    solution = Solution()

    print(solution.removeNthFromEnd([1,2,3,4,5], 2))
