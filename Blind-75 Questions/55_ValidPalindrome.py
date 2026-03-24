"""
Problem: 125_ValidPalindrome
Category: Strings / Two Pointers
Difficulty: Easy
"""

class Solution:

    # --------------------------------------------------
    # Approach 1: Clean + Reverse (Simple)
    # --------------------------------------------------
    def clean_and_reverse(self, s):
        """
        Build cleaned string, then compare with reverse

        Time Complexity: O(n)
        Space Complexity: O(n)

        Why:
        - Easiest to explain
        - Good starting point
        """
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch.lower()

        return cleaned == cleaned[::-1]


    # --------------------------------------------------
    # Approach 2: Two Pointers (Optimal)
    # --------------------------------------------------
    def two_pointers(self, s):
        """
        Compare from both ends, skip non-alphanumeric

        Time Complexity: O(n)
        Space Complexity: O(1)

        Why best:
        - No extra space
        - Most expected in interviews
        """
        left, right = 0, len(s) - 1

        while left < right:

            # skip non-alphanumeric
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            # compare lowercase
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


    # --------------------------------------------------
    # Approach 3: Pythonic (Mention Only)
    # --------------------------------------------------
    def pythonic(self, s):
        """
        Using list comprehension

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]


    # --------------------------------------------------
    # Final (What to say in interview)
    # --------------------------------------------------
    def solve(self, s):
        return self.two_pointers(s)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve("A man, a plan, a canal: Panama"))  # True
    print(sol.solve("race a car"))                      # False