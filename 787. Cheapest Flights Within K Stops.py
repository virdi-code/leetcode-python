# bellman ford modified

# two arrays: one prices and another temp.
# temp merges into the main prices array after a loop through all edges.
# ignore src that are already infinity.

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k+1):
            tmpPrices = prices.copy()
            for s,d,p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices= tmpPrices
        return prices[dst] if prices[dst] != float("inf") else -1
                
