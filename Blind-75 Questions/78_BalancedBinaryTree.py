"""
Problem: 110_BalancedBinaryTree
Category: Tree / DFS
Difficulty: Easy-Medium
"""

# --------------------------
# Definition
# --------------------------
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # --------------------------------------------------
    # 1. Brute Force (Recompute Heights)
    # --------------------------------------------------
    def brute_force(self, root):
        """
        Check balance at every node separately

        Time Complexity: O(n^2)
        Space Complexity: O(h)
        """
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        if not root:
            return True

        left_h = height(root.left)
        right_h = height(root.right)

        if abs(left_h - right_h) > 1:
            return False

        return self.brute_force(root.left) and self.brute_force(root.right)


    # --------------------------------------------------
    # 2. Optimal DFS (Height + Check Together) ⭐
    # --------------------------------------------------
    def optimal(self, root):
        """
        Return height, or -1 if unbalanced

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left, right)

        return dfs(root) != -1


    # --------------------------------------------------
    # 3. Tuple Style (Height + Balanced)
    # --------------------------------------------------
    def tuple_solution(self, root):
        """
        Return (height, isBalanced)

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def dfs(node):
            if not node:
                return (0, True)

            lh, lb = dfs(node.left)
            rh, rb = dfs(node.right)

            height = 1 + max(lh, rh)
            balanced = lb and rb and abs(lh - rh) <= 1

            return (height, balanced)

        return dfs(root)[1]


    # --------------------------------------------------
    # Final (Interview)
    # --------------------------------------------------
    def solve(self, root):
        return self.optimal(root)


# --------------------------
# Helper
# --------------------------
from collections import deque

def print_tree(root):
    if not root:
        print("Empty")
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    # Balanced Tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    print("Balanced:", sol.solve(root1))  # True

    # Unbalanced Tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.left.left = TreeNode(4)

    print("Balanced:", sol.solve(root2))  # False