"""
Problem: 242_ValidAnagram
Category: Strings / Hashing
Difficulty: Easy
"""

class Solution:

    # --------------------------------------------------
    # Approach 1: Sorting
    # --------------------------------------------------
    def sorting(self, s, t):
        """
        Sort both strings and compare

        Time Complexity: O(n log n)
        Space Complexity: O(1) or O(n) depending on sort implementation

        Why interviewers like it:
        - Simple and clean
        - Good starting point
        """
        return sorted(s) == sorted(t)


    # --------------------------------------------------
    # Approach 2: HashMap (Frequency Count)
    # --------------------------------------------------
    def hashmap(self, s, t):
        """
        Count characters using dictionary

        Time Complexity: O(n)
        Space Complexity: O(n)

        Why important:
        - Optimal and general solution
        - Works for any charset (Unicode also)
        """
        if len(s) != len(t):
            return False

        freq = {}

        # count chars in s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # subtract using t
        for ch in t:
            if ch not in freq:
                return False
            freq[ch] -= 1
            if freq[ch] == 0:
                del freq[ch]

        return len(freq) == 0


    # --------------------------------------------------
    # Approach 3: Fixed Array (Best for lowercase letters)
    # --------------------------------------------------
    def array_count(self, s, t):
        """
        Use array of size 26 for lowercase letters

        Time Complexity: O(n)
        Space Complexity: O(1)

        Why best:
        - Most optimal in practice
        - No hashmap overhead
        """
        if len(s) != len(t):
            return False

        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        return all(c == 0 for c in count)


    # --------------------------------------------------
    # Final (What to say in interview)
    # --------------------------------------------------
    def solve(self, s, t):
        return self.array_count(s, t)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve("anagram", "nagaram"))  # True
    print(sol.solve("rat", "car"))          # False