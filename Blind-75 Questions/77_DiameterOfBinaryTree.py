"""
Problem: 543_DiameterOfBinaryTree
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
        For every node, calculate height separately

        Time Complexity: O(n^2)
        Space Complexity: O(h)
        """
        if not root:
            return 0

        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        left_diameter = self.brute_force(root.left)
        right_diameter = self.brute_force(root.right)

        curr_diameter = height(root.left) + height(root.right)

        return max(curr_diameter, left_diameter, right_diameter)


    # --------------------------------------------------
    # 2. Optimal DFS (Best / Most Expected)
    # --------------------------------------------------
    def optimal(self, root):
        """
        Calculate height and diameter in one pass

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        self.diameter = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # update diameter
            self.diameter = max(self.diameter, left + right)

            # return height
            return 1 + max(left, right)

        dfs(root)
        return self.diameter


    # --------------------------------------------------
    # 3. Cleaner (Return tuple)
    # --------------------------------------------------
    def tuple_solution(self, root):
        """
        Return (height, diameter)

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        def dfs(node):
            if not node:
                return (0, 0)  # height, diameter

            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)

            height = 1 + max(lh, rh)
            diameter = max(lh + rh, ld, rd)

            return (height, diameter)

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

    # Create tree:
    #        1
    #      /   \
    #     2     3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Tree:")
    print_tree(root)

    print("Diameter:", sol.solve(root))  # 3