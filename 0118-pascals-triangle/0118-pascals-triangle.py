class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res=[[1]]
        old=[1,1]
        if numRows<2:
            return res
        if numRows>=2:
            res.append([1,1])
        for i in range(3,numRows+1):
            new=[0]*i
            new[0]=1
            new[-1]=1
            for j in range(1,i-1):
                new[j]=old[j-1]+old[j]
            if new!=[]:
                res.append(new)
            old[:]=new[:]
        return res

