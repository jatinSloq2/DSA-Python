"""
Problem: 21_MergeTwoSortedLists
Category: Linked List
Difficulty: Easy
"""

# --------------------------
# Definition
# --------------------------
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # --------------------------------------------------
    # 1. Brute Force (Array + Sort)
    # --------------------------------------------------
    def brute_force(self, l1, l2):
        """
        Time Complexity: O((n+m) log(n+m))
        Space Complexity: O(n+m)
        """
        vals = []

        while l1:
            vals.append(l1.val)
            l1 = l1.next

        while l2:
            vals.append(l2.val)
            l2 = l2.next

        vals.sort()

        dummy = ListNode(0)
        curr = dummy

        for v in vals:
            curr.next = ListNode(v)
            curr = curr.next

        return dummy.next


    # --------------------------------------------------
    # 2. Iterative (Best / Interview)
    # --------------------------------------------------
    def iterative(self, l1, l2):
        """
        Time Complexity: O(n+m)
        Space Complexity: O(1)
        """
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        # attach remaining list
        tail.next = l1 if l1 else l2

        return dummy.next


    # --------------------------------------------------
    # 3. Recursive
    # --------------------------------------------------
    def recursive(self, l1, l2):
        """
        Time Complexity: O(n+m)
        Space Complexity: O(n+m)
        """
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.recursive(l1, l2.next)
            return l2


    # --------------------------------------------------
    # Final (Use in interview)
    # --------------------------------------------------
    def solve(self, l1, l2):
        return self.iterative(l1, l2)


# --------------------------
# Helper Functions
# --------------------------
def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    # Create list 1: 1 -> 3 -> 5
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(5)

    # Create list 2: 2 -> 4 -> 6
    l2 = ListNode(2)
    l2.next = ListNode(4)
    l2.next.next = ListNode(6)

    print("List 1:")
    print_list(l1)

    print("List 2:")
    print_list(l2)

    merged = sol.solve(l1, l2)

    print("Merged:")
    print_list(merged)