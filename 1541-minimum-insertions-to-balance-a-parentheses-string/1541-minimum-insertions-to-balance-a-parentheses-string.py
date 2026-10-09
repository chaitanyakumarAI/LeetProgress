class Solution:
    def minInsertions(self, s: str) -> int:
        n=len(s)
        i=0
        bc=0
        ins=0
        while i<n:
            if s[i]=='(':
                bc+=2
                i+=1
            else:
                if i+1<n and s[i+1]==')':
                    bc-=2
                    i+=2
                else:
                    ins+=1
                    i+=1
                    bc-=2
                if bc<0:
                    ins+=1
                    bc+=2
        return ins+bc