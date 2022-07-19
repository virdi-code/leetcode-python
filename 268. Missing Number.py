#logic  7^7 = 0   ....  0 ^7 = 7



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        listt = list(i for i in range(n+1)) 
        a= reduce(lambda x,y : x^ y ,nums )
        b= reduce(lambda x,y : x^ y ,listt )
        return a^b
