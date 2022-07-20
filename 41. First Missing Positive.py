# [3,4,-1,1] 
# [3,4,0,1]
# [-3, 4, -5, -1]
# > 2

# remove negative values, make em zero
# store vals in array as negative value
# 0 changes to negative n+1





class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            val = abs(nums[i])
            if 1<= val <= n :
                if nums[val -1] >0:
                    nums[val-1] = -1 * nums[val-1]
                elif nums[val-1] ==0:
                    nums[val - 1]= -(n+1)
        for i in  range(1,n+1):
            if nums[i-1] >= 0 :
                return i
        return n+1
    
       
        
