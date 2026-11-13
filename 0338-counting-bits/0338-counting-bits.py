class Solution:
    def countBits(self, n: int) -> list[int]:
        res=[0]
        def countone(n):
            c=0
            while n!=0:
                if n%2==1:
                    c+=1
                n=n//2
            return c
        for i in range(1,n+1):
            res.append(countone(i))
        return res