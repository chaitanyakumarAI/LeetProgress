class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        if n==1:
            return 0
        ma=[0]*(n-1)
        m=float('inf')
        mx=0
        for i in range(n-1):
            m=min(m,prices[i])
            ma[i]=m
            mx=max(prices[i+1]-ma[i],mx)
        return mx