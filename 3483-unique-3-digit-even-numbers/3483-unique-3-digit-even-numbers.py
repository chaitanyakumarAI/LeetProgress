class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)
        count=0
        snums=set()
        for i in range(n):
            if digits[i]!=0:
                for j in range(n):
                    for k in range(n):
                        if i!=j and j!=k and i!=k and digits[k]%2==0:
                            num=digits[i]*100+digits[j]*10+digits[k]
                            if num not in snums:
                                snums.add(num)
                                count+=1
        return count
