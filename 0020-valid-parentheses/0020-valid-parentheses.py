class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        f=0
        st=[]
        if n%2==1:
            return False
        for i in range(n):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                st.append(s[i])
                f=1
            else:
                if ( s[i]==')' )and (st==[] or st.pop()!='('):
                    return False
                elif ( s[i]==']' ) and (st==[] or st.pop()!='['):
                    return False
                elif ( s[i]=='}' ) and (st==[] or st.pop()!='{'):
                    return False
                f=0
        if f==1 or st!=[]:
            return False
        return True