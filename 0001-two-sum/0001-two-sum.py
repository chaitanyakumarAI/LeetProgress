class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        
        l=0
        r=n-1
        ret=[]
        count={}
        for i,e in enumerate(nums):
            if e in count:
                count[e].append(i)
            else:
                count[e]=[i]
        print count
        nums.sort()
        while l<r:
            if nums[l]+nums[r]==target:
                ret.append(count[nums[l]][0])
                if nums[l]==nums[r]:
                    ret.append(count[nums[r]][1])
                else:
                    ret.append(count[nums[r]][0])
                break
            elif nums[l]+nums[r]<target:
                l+=1
            else:
                r-=1
        return ret
