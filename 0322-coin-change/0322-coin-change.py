class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        if amount==0:
            return 0
        for coin in coins:
            if coin<=amount:
                dp[coin]=1
        for i in range(2,amount+1):
            for coin in coins:
                if i-coin>0:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        if dp[-1]==float('inf'):
            return -1
        return dp[-1]