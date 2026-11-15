class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        n=len(arr)
        cs=0
        os=0
        es=1
        c=0
        for i in range(n):
            cs+=arr[i]
            if cs%2==1:
                c+=es
                os+=1
            else:
                c+=os
                es+=1
        return c%(pow(10,9)+7)