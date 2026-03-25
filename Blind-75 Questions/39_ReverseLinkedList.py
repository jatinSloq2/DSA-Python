"""
Problem: 206_ReverseLinkedList
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
    # 1. Brute Force (Using Array)
    # --------------------------------------------------
    def brute_force(self, head):
        """
        Store values and rewrite

        Time Complexity: O(n)
        Space Complexity: O(n)

        Note:
        - Not preferred (doesn't reverse links)
        """
        vals = []
        curr = head

        while curr:
            vals.append(curr.val)
            curr = curr.next

        curr = head
        while curr:
            curr.val = vals.pop()
            curr = curr.next

        return head


    # --------------------------------------------------
    # 2. Iterative (Best / Most Expected)
    # --------------------------------------------------
    def iterative(self, head):
        """
        Reverse pointers

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next
            curr.next = prev     # reverse link
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev


    # --------------------------------------------------
    # 3. Recursive
    # --------------------------------------------------
    def recursive(self, head):
        """
        Reverse using recursion

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head or not head.next:
            return head

        newHead = self.recursive(head.next)

        head.next.next = head
        head.next = None

        return newHead


    # --------------------------------------------------
    # 4. Stack-Based (Extra DS)
    # --------------------------------------------------
    def stack_based(self, head):
        """
        Use stack to reverse nodes

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head:
            return head

        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next

        new_head = stack.pop()
        curr = new_head

        while stack:
            curr.next = stack.pop()
            curr = curr.next

        curr.next = None
        return new_head


    # --------------------------------------------------
    # Final (Interview)
    # --------------------------------------------------
    def solve(self, head):
        return self.iterative(head)


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

    # Create: 1 -> 2 -> 3 -> 4 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)

    print("Original:")
    print_list(head)

    reversed_head = sol.solve(head)

    print("Reversed:")
    print_list(reversed_head)