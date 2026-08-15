class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        req=0
        n=len(s)
        for i in range(1,n):
            for j in range(i):
                occ={}
                for k in range(j,i+1):
                    if s[k] in occ:
                        occ[s[k]]+=1
                    else:
                        occ[s[k]]=1
                if all(value <=2 for value in occ.values()):
                    req=max(req,i-j+1)
        return req