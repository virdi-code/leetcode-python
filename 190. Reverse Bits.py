# move n by [0,1,2,3....
# and it with 1.
# build new bitstring with 1 <<i 
# OR it with result.

class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        for i in range(32):
            bit = 1 & (n>>i)
            res = res | (bit << (31 -i))
        return res
