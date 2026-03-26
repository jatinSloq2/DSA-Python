"""
Problem: 141_LinkedListCycle
Category: Linked List / Two Pointers
Difficulty: Easy
"""

# --------------------------
# Definition
# --------------------------
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # --------------------------------------------------
    # 1. Brute Force (HashSet)
    # --------------------------------------------------
    def hashset(self, head):
        """
        Store visited nodes

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            seen.add(curr)
            curr = curr.next

        return False


    # --------------------------------------------------
    # 2. Floyd’s Cycle Detection (Best)
    # --------------------------------------------------
    def two_pointer(self, head):
        """
        Fast & Slow pointers

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


    # --------------------------------------------------
    # 3. Mark Visited (Modify Nodes - not preferred)
    # --------------------------------------------------
    def mark_visited(self, head):
        """
        Modify node values or pointers

        Time Complexity: O(n)
        Space Complexity: O(1)

        Note:
        - Not safe (modifies input)
        """
        curr = head

        while curr:
            if curr.val == "visited":
                return True

            curr.val = "visited"
            curr = curr.next

        return False


    # --------------------------------------------------
    # Final (Interview)
    # --------------------------------------------------
    def solve(self, head):
        return self.two_pointer(head)


# --------------------------
# Helper
# --------------------------
def print_list(head, limit=10):
    """
    Print limited nodes to avoid infinite loop
    """
    curr = head
    count = 0

    while curr and count < limit:
        print(curr.val, end=" -> ")
        curr = curr.next
        count += 1

    print("..." if curr else "None")


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    # Create list: 1 -> 2 -> 3 -> 4
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)

    head.next = second
    second.next = third
    third.next = fourth

    # Case 1: No cycle
    print("No Cycle:", sol.solve(head))  # False

    # Case 2: Create cycle (4 -> 2)
    fourth.next = second

    print("Cycle:", sol.solve(head))     # True