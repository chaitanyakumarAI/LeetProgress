class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        old=[1,1]
        if rowIndex<1:
            return [1]
        if rowIndex==1:
            return old
        for i in range(3,rowIndex+2):
            new=[0]*i
            new[0]=1
            new[-1]=1
            for j in range(1,i-1):
                new[j]=old[j-1]+old[j]
            old[:]=new[:]
        return new