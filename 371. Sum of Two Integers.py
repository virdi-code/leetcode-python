# ADD is equivalent to {xor} and addition of {and} bit shifted by 1
#   1001
#   1011
#^  0010   <- add
#&  1001   bit shift right
#  10010   <- add
#  10100   <-ans

class Solution:
    def getSum(self, a: int, b: int) -> int:
        And = a & b
        if not And:
            return a^ b
        mask = 0xFFFFFFFF
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        while b:
            xor = a^b
            toadd = (a&b)<<1
            a = xor&mask
            b = toadd&mask
            And = a & b
        return a if a <= MAX else ~(a ^ mask)
            
