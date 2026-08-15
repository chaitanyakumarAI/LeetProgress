class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        ma=[0]*(n-1)
        m=float('inf')
        for i in range(n-1):
            m=min(m,prices[i])
            ma[i]=m
        mx=0
        for i in range(1,n):
            mx=max(prices[i]-ma[i-1],mx)
        return mx