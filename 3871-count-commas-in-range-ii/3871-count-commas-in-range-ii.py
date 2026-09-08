class Solution:
    def countCommas(self, n: int) -> int:
        if n<1000:
            return 0
        div=1000
        count=0
        while n>=div:
            count+=n-div+1
            div*=1000
        return count
