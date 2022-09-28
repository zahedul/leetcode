from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> \
    Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        while list2:
            node_a, node_b = list1, list2
            list2 = list2.next

            if node_b.val <= node_a.val:
                node_b.next = node_a
                list1 = node_b
            else:
                prev = None
                while node_a is not None and node_b.val > node_a.val:
                    prev = node_a
                    node_a = node_a.next

                temp = prev.next
                prev.next = node_b
                node_b.next = temp

        return list1


if __name__ == "__main__":
    solution = Solution()

    print(solution.mergeTwoLists([1, 2, 4], [1, 3, 4]))
