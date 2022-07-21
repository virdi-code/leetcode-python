class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)
        if(a != b ):
            return false
        
        cS, cT = {},{}
        
        for i in range(a):
            cS[s[i]] = cS.get(s[i],0) + 1
            cT[t[i]] = cT.get(t[i],0) + 1
            
        for key in cS:
            if cS[key] == cT.get(key,0):
                pass
            else:
                return False
        return True
      
      
      

# 2 : Using Counter
from collections import Counter

class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
          return Counter(s) == Counter(t)
      
      
      
# 3 : Assuming Sorting uses no extra memory. Solving in O(1) memory.
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
          return sorted(s) == sorted(t)
