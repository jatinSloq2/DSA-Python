import os

questions = [
"01_TwoSum",
"02_BestTimeToBuyAndSellStock",
"03_ContainsDuplicate",
"04_ProductOfArrayExceptSelf",
"05_MaximumSubarray",
"06_MaximumProductSubarray",
"07_FindMinimumInRotatedSortedArray",
"08_SearchInRotatedSortedArray",
"09_3Sum",
"10_ContainerWithMostWater",

"11_SumOfTwoIntegers",
"12_NumberOf1Bits",
"13_CountingBits",
"14_MissingNumber",
"15_ReverseBits",

"16_ClimbingStairs",
"17_CoinChange",
"18_LongestIncreasingSubsequence",
"19_LongestCommonSubsequence",
"20_WordBreak",
"21_CombinationSum",
"22_HouseRobber",
"23_HouseRobberII",
"24_DecodeWays",
"25_UniquePaths",

"26_CloneGraph",
"27_CourseSchedule",
"28_PacificAtlanticWaterFlow",
"29_NumberOfIslands",
"30_LongestConsecutiveSequence",

"31_AlienDictionary",
"32_GraphValidTree",
"33_NumberOfConnectedComponents",

"34_InsertInterval",
"35_MergeIntervals",
"36_NonOverlappingIntervals",
"37_MeetingRooms",
"38_MeetingRoomsII",

"39_ReverseLinkedList",
"40_LinkedListCycle",
"41_MergeTwoSortedLists",
"42_MergeKSortedLists",
"43_RemoveNthNodeFromEnd",
"44_ReorderList",

"45_SetMatrixZeroes",
"46_SpiralMatrix",
"47_RotateImage",
"48_WordSearch",

"49_LongestSubstringWithoutRepeatingCharacters",
"50_LongestRepeatingCharacterReplacement",
"51_MinimumWindowSubstring",
"52_ValidAnagram",
"53_GroupAnagrams",

"54_ValidParentheses",
"55_ValidPalindrome",
"56_LongestPalindromicSubstring",
"57_PalindromicSubstrings",

"58_EncodeAndDecodeStrings",

"59_MaximumDepthOfBinaryTree",
"60_SameTree",
"61_InvertBinaryTree",
"62_BinaryTreeMaximumPathSum",
"63_BinaryTreeLevelOrderTraversal",
"64_SerializeAndDeserializeBinaryTree",
"65_SubtreeOfAnotherTree",
"66_ConstructBinaryTreeFromPreorderAndInorder",
"67_ValidateBinarySearchTree",
"68_KthSmallestElementInBST",
"69_LowestCommonAncestorOfBST",

"70_ImplementTrie",
"71_AddAndSearchWord",
"72_WordSearchII",

"73_TopKFrequentElements",
"74_FindMedianFromDataStream",
"75_LRUCache"
]

base_path = "questions"
os.makedirs(base_path, exist_ok=True)

template = '''"""
Problem: {name}
Category:
Difficulty:
Link:

Notes:
- Approach:
- Time Complexity:
- Space Complexity:
"""

class Solution:
    def solve(self, *args):
        pass


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.solve())
'''

for q in questions:
    file_path = os.path.join(base_path, f"{q}.py")
    
    # avoid overwrite if file exists
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(template.format(name=q))
    else:
        print(f"Skipped (already exists): {q}.py")

print("✅ All 75 files created in /questions folder 🚀")