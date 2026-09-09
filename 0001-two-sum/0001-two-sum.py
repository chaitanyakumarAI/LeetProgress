class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dnums={item:index for index,item in enumerate(nums)}
        for i in range(len(nums)):
            if target-nums[i] in dnums and i!=dnums[target-nums[i]]:
                return [i,dnums[target-nums[i]]]
        