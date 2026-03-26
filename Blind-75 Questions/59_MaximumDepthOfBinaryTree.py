"""
Problem: 104_MaximumDepthOfBinaryTree
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
        Height = 1 + max(left, right)

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0

        left = self.recursive(root.left)
        right = self.recursive(root.right)

        return 1 + max(left, right)


    # --------------------------------------------------
    # 2. Iterative DFS (Stack)
    # --------------------------------------------------
    def dfs_stack(self, root):
        """
        Use stack with depth tracking

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return max_depth


    # --------------------------------------------------
    # 3. BFS (Level Order)
    # --------------------------------------------------
    def bfs(self, root):
        """
        Count levels

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not root:
            return 0

        from collections import deque
        queue = deque([root])
        depth = 0

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            depth += 1

        return depth


    # --------------------------------------------------
    # 4. Compact One-Liner (Recursive)
    # --------------------------------------------------
    def one_liner(self, root):
        """
        Short recursive form

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        return 1 + max(self.one_liner(root.left), self.one_liner(root.right)) if root else 0


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
    #        3
    #      /   \
    #     9     20
    #          /  \
    #         15   7

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Tree:")
    print_tree(root)

    print("Max Depth:", sol.solve(root))  # 3