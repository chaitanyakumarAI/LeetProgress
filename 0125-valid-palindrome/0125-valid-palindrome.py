class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        clean = ""

        for c in s:
            if c.isalnum():
                clean += c.lower()
        s=clean
        if s==''  or len(s)==1:
            return True
        for i in range(0,(len(s)//2)+1):
            if s[i]!=s[len(s)-1-i]:
                return False
        return True
