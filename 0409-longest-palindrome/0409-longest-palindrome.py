class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq={}
        n=len(s)
        for i in range(n):
            if s[i] not in freq:
                freq[s[i]]=1
            else:
                freq[s[i]]+=1
        req=0
        has_odd=0
        for val in freq.values():
            if val%2==0:
                req+=val
            else:
                has_odd=1
                req+=val-1
        if has_odd==1:
            req+=1
        return req