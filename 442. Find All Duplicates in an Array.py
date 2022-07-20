# need to do in single pass.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]

# solution:
# iterate over array
# take i , put it as -i in temp array.
# if already negative add to answer array.


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        temp =[0] * (len(nums)+1)
        ans = list()
        for i in nums:
            if temp[i] == 0:
                temp[i] = -i
            else : ans.append(i)
            
        return ans
