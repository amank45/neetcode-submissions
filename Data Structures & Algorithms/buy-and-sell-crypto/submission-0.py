class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bi = prices[0]
        ans = 0

        for i in range(1, n):
            if prices[i] < bi:
                bi = prices[i]

            ans = max(ans, prices[i] - bi)

        return ans

        