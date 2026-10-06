class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st=[]
        c=0
        for i in s:
            if i=='(':
                st.append(i)
            elif st!=[]:
                st.pop()
            else:
                c+=1
        return c+len(st)