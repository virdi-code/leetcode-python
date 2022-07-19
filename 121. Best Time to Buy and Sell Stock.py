class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = []
        n = len(prices)
        lmin = 999999
        for i in range(len(prices)):
            lmin = min(lmin,prices[i])
            nums.append(lmin)
            prices[i] = prices[i] -lmin
        if lmin == 999999:
            return 0
        return max(prices)
        
