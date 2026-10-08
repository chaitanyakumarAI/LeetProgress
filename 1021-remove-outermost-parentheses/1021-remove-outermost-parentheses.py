class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=""
        temp=""
        st=[]
        for i in s:
            if i=="(" :
                if st==[]:
                    res+=temp
                    temp=""
                else:
                    temp+=i
                st.append(i)
            else:
                st.pop()
                if st!=[]:
                    temp+=i
                
        if temp!="":
            res+=temp
        return res
                    
                    

                
            