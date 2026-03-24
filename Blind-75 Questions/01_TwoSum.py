"""
Problem: 01_TwoSum
Category: Arrays / Hashing
Difficulty: Easy
"""

class Solution:

    # --------------------------------------------------
    # Approach 1: Brute Force
    # --------------------------------------------------
    def brute_force(self, nums, target):
        """
        Try all pairs

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Why:
        - Good starting point in interview
        """
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]


    # --------------------------------------------------
    # Approach 2: HashMap (Optimal)
    # --------------------------------------------------
    def hashmap(self, nums, target):
        """
        Store value → index

        Time Complexity: O(n)
        Space Complexity: O(n)

        Why best:
        - Single pass
        - Most expected solution
        """
        seen = {}  # value -> index

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i


    # --------------------------------------------------
    # Approach 3: Two Pointers (After Sorting)
    # --------------------------------------------------
    def two_pointers(self, nums, target):
        """
        Sort + two pointers

        Time Complexity: O(n log n)
        Space Complexity: O(n) (to preserve indices)

        Why asked:
        - Tests understanding of two-pointer pattern
        - Requires handling indices carefully
        """
        arr = list(enumerate(nums))  # (index, value)
        arr.sort(key=lambda x: x[1])

        left, right = 0, len(arr) - 1

        while left < right:
            curr_sum = arr[left][1] + arr[right][1]

            if curr_sum == target:
                return [arr[left][0], arr[right][0]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1


    # --------------------------------------------------
    # Final (What to say in interview)
    # --------------------------------------------------
    def solve(self, nums, target):
        return self.hashmap(nums, target)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve([2, 7, 11, 15], 9))   # [0, 1]
    print(sol.solve([3, 2, 4], 6))        # [1, 2]