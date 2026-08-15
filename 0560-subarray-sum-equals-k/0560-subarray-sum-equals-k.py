class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sums={0:1}
        c=0
        cs=0
        for num in nums:
            cs+=num
            target=cs-k
            if target in prefix_sums:
                c+=prefix_sums[target]
            prefix_sums[cs]=prefix_sums.get(cs,0)+1
        return c