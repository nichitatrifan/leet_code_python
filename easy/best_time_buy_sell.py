# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and
# choosing a different day in the future to sell that stock.

# RETURN MAX PROFIT you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List, Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        right = 1
        left = 0
        best_profit = 0
        arr_len = len(prices) - 1

        while right <= arr_len:
            current_profit = prices[right] - prices[left]
            if current_profit < 0 :
                left += 1
                if left == right:
                    right += 1
            elif current_profit > best_profit:
                best_profit = current_profit
                right += 1
            elif current_profit <= best_profit:
                right += 1

        return best_profit

    def maxProfit_not_efficient(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        best_profit : Optional[int] = None
        current_day : int

        for i, day in enumerate(prices):
            for next_day in prices[i + 1 :]:
                current_day = next_day - day
                if best_profit is None:
                    best_profit = current_day
                elif current_day > best_profit:
                    best_profit = current_day

        if best_profit < 0:
            return 0
        else:
            return best_profit

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))
    print(solution.maxProfit([2,1,4]))