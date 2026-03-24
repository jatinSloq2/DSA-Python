"""
Problem: BestTimeToBuyAndSellStock
Category: Arrays / Greedy
Difficulty: Easy
"""

class Solution:

    # --------------------------------------------------
    # Approach 1: Brute Force
    # --------------------------------------------------
    def brute_force(self, prices):
        """
        Try all pairs (buy before sell)

        Time Complexity: O(n^2)
        Space Complexity: O(1)

        Why:
        - Good starting explanation
        """
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit


    # --------------------------------------------------
    # Approach 2: Greedy (Optimal)
    # --------------------------------------------------
    def optimal(self, prices):
        """
        Track minimum price and max profit

        Time Complexity: O(n)
        Space Complexity: O(1)

        Why best:
        - Single pass
        - Most expected solution
        """
        min_price = float('inf')
        max_profit = 0

        for price in prices:

            # update minimum price seen so far
            if price < min_price:
                min_price = price

            # calculate profit if sold today
            profit = price - min_price

            # update max profit
            if profit > max_profit:
                max_profit = profit

        return max_profit


    # --------------------------------------------------
    # Final
    # --------------------------------------------------
    def solve(self, prices):
        return self.optimal(prices)


# --------------------------
# Test Cases
# --------------------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.solve([7,1,5,3,6,4]))  # 5
    print(sol.solve([7,6,4,3,1]))    # 0