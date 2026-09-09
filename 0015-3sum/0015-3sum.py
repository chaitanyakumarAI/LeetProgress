class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        target=0
        res=[]
        for i in range(n):
            if i>0 and nums[i]==nums[i-1]:
                    continue  
            if nums[i]>0:
                break
            l=i+1
            r=n-1
            while (l<r):               
                if nums[r]<0:
                    break
                sm=nums[l]+nums[r]+nums[i]
                if sm==target:
                    res.append([nums[l],nums[r],nums[i]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    l+=1
                    r-=1
                elif sm<target:
                    l+=1
                else:
                    r-=1
        return res