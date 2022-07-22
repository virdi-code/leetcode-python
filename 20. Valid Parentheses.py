class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        dict = {"]":"[", "}":"{", ")":"("}
        for i in s:
            if i =="(" or i == "{" or i == "[":
                st.append(i)
            else :
                if not st:
                    return False
                if st.pop() == dict[i]:
                    continue
                else: return False
                
        if not st:
            return True
        else : return False
