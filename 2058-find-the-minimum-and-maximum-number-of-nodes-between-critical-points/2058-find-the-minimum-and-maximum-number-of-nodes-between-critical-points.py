# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev=head
        pres=prev.next
        nex=pres.next
        if nex==None:
            return [-1,-1]
        cp=[]
        index=1
        while nex!=None:
            if (pres.val>prev.val and pres.val>nex.val) or (pres.val<prev.val and pres.val<nex.val):
                cp.append(index)
            index+=1
            prev=prev.next
            pres=prev.next
            nex=pres.next
        n=len(cp)
        if n<2:
            return[-1,-1]
        cp.sort()
        md=min(cp[i+1]-cp[i] for i in range(n-1))
        return [md,max(cp)-min(cp)]