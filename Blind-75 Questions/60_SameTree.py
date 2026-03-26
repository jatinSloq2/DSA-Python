"""
Problem: 100_SameTree
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
    def recursive(self, p, q):
        """
        Compare nodes recursively

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        # both null
        if not p and not q:
            return True

        # one null or value mismatch
        if not p or not q or p.val != q.val:
            return False

        # check left & right
        return self.recursive(p.left, q.left) and \
               self.recursive(p.right, q.right)


    # --------------------------------------------------
    # 2. Iterative DFS (Stack)
    # --------------------------------------------------
    def dfs_stack(self, p, q):
        """
        Use stack to compare nodes

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        stack = [(p, q)]

        while stack:
            n1, n2 = stack.pop()

            if not n1 and not n2:
                continue

            if not n1 or not n2 or n1.val != n2.val:
                return False

            stack.append((n1.left, n2.left))
            stack.append((n1.right, n2.right))

        return True


    # --------------------------------------------------
    # 3. BFS (Queue)
    # --------------------------------------------------
    def bfs(self, p, q):
        """
        Level order comparison

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        from collections import deque

        queue = deque([(p, q)])

        while queue:
            n1, n2 = queue.popleft()

            if not n1 and not n2:
                continue

            if not n1 or not n2 or n1.val != n2.val:
                return False

            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))

        return True


    # --------------------------------------------------
    # 4. Compact Version
    # --------------------------------------------------
    def compact(self, p, q):
        """
        Short recursive

        Time Complexity: O(n)
        Space Complexity: O(h)
        """
        return (p and q and p.val == q.val and
                self.compact(p.left, q.left) and
                self.compact(p.right, q.right)) or (p is None and q is None)


    # --------------------------------------------------
    # Final (Interview)
    # --------------------------------------------------
    def solve(self, p, q):
        return self.recursive(p, q)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    # Tree 1
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree 2 (same)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    print("Same:", sol.solve(p, q))   # True

    # Tree 3 (different)
    q2 = TreeNode(1)
    q2.left = TreeNode(2)

    print("Same:", sol.solve(p, q2))  # False