class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        n=len(triangle)
        m=1
        for i in range(1,n):
            m+=1
            for j in range(m):
                if j!=0 and j!=m-1:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
                else:
                    if j==0:
                        triangle[i][j]+=triangle[i-1][j]
                    else:
                        triangle[i][j]+=triangle[i-1][j-1]
        return min(triangle[n-1])
                