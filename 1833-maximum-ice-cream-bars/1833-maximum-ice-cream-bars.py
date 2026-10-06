class Solution:
    def maxIceCream(self, costs: list[int], coins: int) -> int:
        max_cost=max(costs)
        freq=[0]*(max_cost+1)
        if min(costs)>coins:
            return 0
        if sum(costs)<coins:
            return len(costs)
        for i in range(len(costs)):
            freq[costs[i]]+=1
        count=0
        for i in range(1,max_cost+1):
            while freq[i]>0 and coins>=i:
                coins-=i
                freq[i]-=1
                count+=1
            if coins<i:
                break
        return count
            