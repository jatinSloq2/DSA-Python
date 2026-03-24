"""
Problem: 03_ContainsDuplicate
Category: Arrays / Hashing
Difficulty: Easy

Key Insight:
- Trade-off between time and space
"""

class Solution:

    # --------------------------------------------------
    # Approach 1: HashSet (Most Expected / Optimal)
    # --------------------------------------------------
    def hash_set(self, nums):
        """
        Use a set to track seen elements

        Time Complexity: O(n)
        Space Complexity: O(n)

        Why interviewers like it:
        - Optimal solution
        - Shows understanding of hashing
        """
        seen = set()

        for num in nums:
            if num in seen:   # O(1) lookup
                return True
            seen.add(num)

        return False


    # --------------------------------------------------
    # Approach 2: Sorting
    # --------------------------------------------------
    def sorting(self, nums):
        """
        Sort and check adjacent elements

        Time Complexity: O(n log n)
        Space Complexity: O(1) (if in-place sort)

        Why useful:
        - No extra memory
        - Good when space is constrained
        """
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


    # --------------------------------------------------
    # Approach 3: HashMap (Frequency Count)
    # --------------------------------------------------
    def hashmap(self, nums):
        """
        Count frequency using dictionary

        Time Complexity: O(n)
        Space Complexity: O(n)

        Why asked:
        - Extends easily to "find frequency" problems
        """
        freq = {}

        for num in nums:
            if num in freq:
                return True
            freq[num] = 1

        return False


    # --------------------------------------------------
    # Approach 4: One-liner (Mention Only, Not Primary)
    # --------------------------------------------------
    def one_liner(self, nums):
        """
        Pythonic shortcut

        Time Complexity: O(n)
        Space Complexity: O(n)

        Note:
        - Good to mention, but explain HashSet in interview
        """
        return len(nums) != len(set(nums))


    # --------------------------------------------------
    # Final (what you should actually say in interview)
    # --------------------------------------------------
    def solve(self, nums):
        return self.hash_set(nums)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve([1, 2, 3, 4]))   # False
    print(sol.solve([1, 2, 3, 1]))   # True