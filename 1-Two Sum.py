# using hashmap

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasmap = {}
        
        for i,val in enumerate(nums):
            need = target -val
            if need in hasmap:
                return i,hasmap[need]
            else:
                hasmap[val] = i 
        
        
# using two pointers
# nums need to be in sorted order.
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            if nums[l] + nums[r] == target:
                return l,r
            if nums[l] + nums [r] <target:
                l += 1
            if nums[l] + nums [r] > target:
                r -= 1
