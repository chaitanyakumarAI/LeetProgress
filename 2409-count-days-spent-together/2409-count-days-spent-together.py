class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aam=int(arriveAlice[0:2])
        lam=int(leaveAlice[0:2])
        aad=int(arriveAlice[3:5])
        lad=int(leaveAlice[3:5])
        abm=int(arriveBob[0:2])
        lbm=int(leaveBob[0:2])
        abd=int(arriveBob[3:5])
        lbd=int(leaveBob[3:5])
        dpm=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count=0
        aav=0
        for i in range(aam-1):
            aav+=dpm[i]
        aav+=aad
        lav=0
        for i in range(lam-1):
            lav+=dpm[i]
        lav+=lad
        abv=0
        for i in range(abm-1):
            abv+=dpm[i]
        abv+=abd
        lbv=0
        for i in range(lbm-1):
            lbv+=dpm[i]
        lbv+=lbd
        return max(0,min(lav,lbv)-max(aav,abv)+1)