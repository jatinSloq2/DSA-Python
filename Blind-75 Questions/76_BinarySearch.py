# The `Solution` class provides implementations of binary search algorithms, including iterative and
# recursive versions, to find the index of a target value in a given array.
# The `Solution` class provides implementations of binary search algorithms, including iterative and
# recursive versions, to find the index of a target value in a given array.
"""
Problem: 704_BinarySearch
Category: Arrays / Binary Search
Difficulty: Easy
"""

class Solution:

    # --------------------------------------------------
    # 1. Brute Force (Linear Search)
    # --------------------------------------------------
    def brute_force(self, nums, target):
        """
        Scan entire array

        Time Complexity: O(n)
        Space Complexity: O(1)

        Why:
        - Baseline approach
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


    # --------------------------------------------------
    # 2. Binary Search (Iterative) ✅ BEST
    # --------------------------------------------------
    def binary_search(self, nums, target):
        """
        Divide search space in half

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Why best:
        - Most expected in interviews
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


    # --------------------------------------------------
    # 3. Binary Search (Recursive)
    # --------------------------------------------------
    def binary_recursive(self, nums, target, left, right):
        """
        Recursive version

        Time Complexity: O(log n)
        Space Complexity: O(log n) (call stack)
        """
        if left > right:
            return -1

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.binary_recursive(nums, target, mid + 1, right)
        else:
            return self.binary_recursive(nums, target, left, mid - 1)


    # --------------------------------------------------
    # Final
    # --------------------------------------------------
    def solve(self, nums, target):
        return self.binary_search(nums, target)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve([-1,0,3,5,9,12], 9))  
    print(sol.solve([-1,0,3,5,9,12], 2))   # -1