class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # corner case
        if not citations:
            return 0
        if len(citations) == 1:
            return int(citations[0] >=1)
        if citations[-1] < 1:
            return 0
        
        if len(citations) == 2:
            if citations[0] <2 :
                return 1
            else:
                return 2
        
        l, r, n = 0, len(citations)-1, len(citations)
        while l+1 < r:
            mid = (l+r)//2
            # if citations[mid] == mid = 1
            if citations[mid] <= n-mid:
                l = mid
            else:
                r = mid
        if citations[l] >= n-l:
            return n-l
        else:
            return n-r
