# get the LSB and divide by 2.
# get the number of 1 for the new number from the ans array.



class Solutionslow:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            res = 0        
            while i:
                res += i%2
                i = i >> 1
            ans.append(res)
        return ans

      
class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        ans.append(0)
        for i in range(1,n+1):
            res = 0        
            res += i%2
            i = i >> 1
            res += ans[i]
            ans.append(res)
        return ans
