"""
Problem: 226_InvertBinaryTree
Category: Tree / DFS / BFS
Difficulty: Easy
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
    # 1. Recursive DFS (Best / Most Expected)
    # --------------------------------------------------
    def recursive(self, root):
        """
        Swap left & right recursively

        Time Complexity: O(n)
        Space Complexity: O(h)  (height of tree)
        """
        if not root:
            return None

        # swap
        root.left, root.right = root.right, root.left

        # recurse
        self.recursive(root.left)
        self.recursive(root.right)

        return root


    # --------------------------------------------------
    # 2. Iterative DFS (Stack)
    # --------------------------------------------------
    def dfs_stack(self, root):
        """
        Use stack for DFS

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return None

        stack = [root]

        while stack:
            node = stack.pop()

            # swap
            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return root


    # --------------------------------------------------
    # 3. BFS (Queue / Level Order)
    # --------------------------------------------------
    def bfs(self, root):
        """
        Level-order traversal

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return None

        from collections import deque
        queue = deque([root])

        while queue:
            node = queue.popleft()

            # swap
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root


    # --------------------------------------------------
    # Final (Interview)
    # --------------------------------------------------
    def solve(self, root):
        return self.recursive(root)


# --------------------------
# Helper (Level Order Print)
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
    #        4
    #      /   \
    #     2     7
    #    / \   / \
    #   1   3 6   9

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original:")
    print_tree(root)

    sol.solve(root)

    print("Inverted:")
    print_tree(root)