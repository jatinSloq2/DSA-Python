# """
# Problem: 20_ValidParentheses
# Category: Stack
# Difficulty: Easy
# """

# class Solution:

#     # --------------------------------------------------
#     # 1. Brute Force (Worst)
#     # --------------------------------------------------
#     def brute_force(self, s):
#         """
#         Remove valid pairs repeatedly

#         Time Complexity: O(n^2)
#         Space Complexity: O(n)
#         """
#         prev = None

#         while prev != s:
#             prev = s
#             s = s.replace("()", "").replace("[]", "").replace("{}", "")

#         return s == ""


#     # --------------------------------------------------
#     # 2. Stack (Basic)
#     # --------------------------------------------------
#     def stack_basic(self, s):
#         """
#         Manual matching

#         Time Complexity: O(n)
#         Space Complexity: O(n)
#         """
#         stack = []

#         for ch in s:
#             if ch in "([{":
#                 stack.append(ch)
#             else:
#                 if not stack:
#                     return False

#                 top = stack.pop()

#                 if (top == '(' and ch != ')') or \
#                    (top == '[' and ch != ']') or \
#                    (top == '{' and ch != '}'):
#                     return False

#         return not stack


#     # --------------------------------------------------
#     # 3. Stack + HashMap (Best / Standard)
#     # --------------------------------------------------
#     def stack_hashmap(self, s):
#         """
#         Clean matching using map

#         Time Complexity: O(n)
#         Space Complexity: O(n)
#         """
#         stack = []
#         mapping = {')': '(', ']': '[', '}': '{'}

#         for ch in s:
#             if ch in mapping.values():
#                 stack.append(ch)
#             else:
#                 if not stack or stack[-1] != mapping[ch]:
#                     return False
#                 stack.pop()

#         return not stack


#     # --------------------------------------------------
#     # 4. Push Expected Closing (Advanced Clean)
#     # --------------------------------------------------
#     def push_expected(self, s):
#         """
#         Push expected closing brackets

#         Time Complexity: O(n)
#         Space Complexity: O(n)
#         """
#         stack = []
#         mapping = {'(': ')', '[': ']', '{': '}'}

#         for ch in s:
#             if ch in mapping:
#                 stack.append(mapping[ch])
#             else:
#                 if not stack or stack.pop() != ch:
#                     return False

#         return not stack


#     # --------------------------------------------------
#     # Final (what to use in interview)
#     # --------------------------------------------------
#     def solve(self, s):
#         return self.stack_hashmap(s)


# # --------------------------
# # Test Cases
# # --------------------------
# if __name__ == "__main__":
#     sol = Solution()

#     print(sol.solve("()"))        # True
#     print(sol.solve("()[]{}"))    # True
#     print(sol.solve("(]"))        # False
#     print(sol.solve("([)]"))      # False
#     print(sol.solve("{[]}"))      # True

def isValid(s):
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    print("Input:", s)

    for c in s:
        print("\nProcessing:", c)

        if c in closeToOpen:
            print("  Closing bracket")
            print("  Stack before:", stack)

            if stack and stack[-1] == closeToOpen[c]:
                print("  Match with:", stack[-1], "→ pop")
                stack.pop()
            else:
                print("  ❌ Mismatch or empty stack")
                return False
        else:
            print("  Opening bracket → push")
            stack.append(c)

        print("  Stack after:", stack)

    print("\nFinal stack:", stack)
    print("Result:", not stack)
    return not stack

# Run it
print(isValid("()[]{}"))   # True
# print(isValid("(]"))       # False