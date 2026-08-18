class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq={}
        n=len(nums)
        for i in range(0,n-k+1):
            window_set = set()
            for j in range(k):
                window_set.add(nums[i + j])
            for num in window_set:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        ans = -1
        for num in freq:
            if freq[num] == 1:
                if num > ans:
                    ans = num
                    
        return ans