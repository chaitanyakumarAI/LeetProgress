class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def recurSum(s,k):
            
            n=len(s)
            if n<=k:
                return s
            sm=0
            st=[]
            for i in range(0,n,k):
                if i+k-1<n:
                    st.append(s[i:i+k])
                else:
                    st.append(s[i:n])
            digits=[]
            for num in st:
                digit=0
                for nm in num:
                    digit+=int(nm)
                digits.append(str(digit))
            
            res=''
            for i in digits:
                res+=i
            if len(res)<=k:
                return res
            else:
                return recurSum(res,k)

        return recurSum(s,k)
            