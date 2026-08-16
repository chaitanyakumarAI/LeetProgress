class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n=len(s)
        m=len(t)
        if s=="":
            return True
        c=0
        for i in range(m):
            if  c<n and t[i]==s[c]:
                c+=1
        if c==n:
            return True
        return False