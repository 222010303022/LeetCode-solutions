class Solution:
    def isValid(self, s: str) -> bool:
        hashm = {')':'(','}':'{',']':'['}
        st = []
        for i in s :
            if i not in hashm :
                st.append(i)
            else:
                if not st :
                    return False
                else :
                    popped = st.pop()
                    if popped != hashm[i]:
                        return False
        return not st