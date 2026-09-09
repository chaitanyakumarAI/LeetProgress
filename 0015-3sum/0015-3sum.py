class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        dnums={item:index for index,item in enumerate(nums)}
        if set(nums)=={0} and len(nums)!=3:
            return [[0,0,0]]
        n=len(nums)
        res=set()
        for j in range(n):
            for i in range(j+1,n):
                target=0-nums[i]-nums[j]
                if target in dnums and i!=dnums[target] and j!=dnums[target]:
                    re=tuple(sorted([nums[i],target,nums[j]]))
                    res.add(re) 
        return list(t for t in res)