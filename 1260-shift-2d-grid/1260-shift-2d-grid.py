class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        flatten=[]
        n=len(grid)
        m=len(grid[0])
        for i in range(n):
            for j in range(m):
                flatten.append(grid[i][j])
        for i in range(k):
            flatten.insert(0,flatten.pop())
        for i in range(n):
            for j in range(m):
                grid[i][j]=flatten[i*m+j]
        return grid