class Solution:
    def rob(self, nums: List[int]) -> int:
        rl ,rll = 0,0
        # rll , rl , now, 
        for i in nums:
            now = max(rll + i, rl) 
            # print(rll+i, rl)
            rl, rll = now, rl  
            #  print(now,rl)
        return max(rl,rll)
            
